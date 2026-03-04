import io
import zipfile

import pandas as pd
import requests

ODBUS_ZIP_URL = "https://www150.statcan.gc.ca/n1/pub/21-26-0003/2023001/ODBus_2023.zip"

ENERGY_NAICS_PREFIXES = (
    "22",   # Utilities
    "211",  # Oil and gas extraction
    "213",  # Support activities for mining, and oil and gas extraction
    "237",  # Heavy and civil engineering construction
    "238",  # Specialty trade contractors
    "5413", # Engineering services
    "5416", # Management / consulting
)


def _safe_str(x) -> str:
    return "" if pd.isna(x) else str(x)


def download_and_extract_odbus(timeout=120) -> pd.DataFrame:
    """Download ODBus ZIP and extract the first CSV inside as a raw dataframe."""

    response = requests.get(ODBUS_ZIP_URL, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    zipped = zipfile.ZipFile(io.BytesIO(response.content))
    csv_names = [name for name in zipped.namelist() if name.lower().endswith(".csv")]

    if not csv_names:
        raise RuntimeError("ODBus ZIP did not contain a CSV file.")

    with zipped.open(csv_names[0]) as csv_file:
        return pd.read_csv(csv_file, dtype=str, low_memory=False)


def filter_odbus(df: pd.DataFrame, target_rows=10000) -> pd.DataFrame:
    """Filter ODBus to Quebec industrial/energy businesses and normalize schema."""

    cols = {col.lower(): col for col in df.columns}

    name_col = cols.get("name") or cols.get("business name") or cols.get("business_name")
    prov_col = cols.get("province") or cols.get("prov")
    naics_col = cols.get("naics") or cols.get("naics code") or cols.get("naics_code")

    if not name_col or not prov_col:
        raise RuntimeError(f"ODBus columns not found. Columns: {list(df.columns)[:30]}")

    working = df.copy()
    working["name"] = working[name_col].map(_safe_str)
    working["province"] = working[prov_col].map(_safe_str)
    working["naics"] = working[naics_col].map(_safe_str) if naics_col else ""

    working = working[working["province"].str.contains("Quebec|Québec|QC", case=False, na=False)]

    clean_naics = working["naics"].str.replace(r"\D", "", regex=True)
    working["naics_ok"] = clean_naics.str.startswith(ENERGY_NAICS_PREFIXES)

    name_lc = working["name"].str.lower()
    keyword_ok = (
        name_lc.str.contains(
            "energy|energie|énergie|power|utility|hydro|renew|solar|wind|grid|pipeline|lng|gaz|oil|petrol",
            na=False,
        )
        | name_lc.str.contains(
            "construction|ingénierie|engineering|procurement|approvisionnement|infrastructure",
            na=False,
        )
    )

    filtered = working[working["naics_ok"] | keyword_ok]

    municipality_col = cols.get("municipality name")
    city_series = filtered[municipality_col].map(_safe_str) if municipality_col else ""

    output = pd.DataFrame(
        {
            "name": filtered["name"],
            "industry": "Energy",
            "subsector": "ODBus",
            "country": "Canada",
            "province": "Quebec",
            "region": "North America",
            "city": city_series,
            "language": "French",
            "services": "",
            "source": "ODBus",
            "naics": filtered["naics"],
        }
    )

    output = output.drop_duplicates(subset=["name"]).reset_index(drop=True)

    if len(output) > target_rows:
        output = output.sample(n=target_rows, random_state=42).reset_index(drop=True)

    return output


def load_fallback_odbus() -> pd.DataFrame:
    """Fallback ODBus-like records for offline/test environments."""

    return pd.DataFrame(
        [
            {
                "name": "Hydro Quebec Supplier Network",
                "industry": "Energy",
                "subsector": "Utilities",
                "country": "Canada",
                "province": "Quebec",
                "region": "North America",
                "city": "Montreal",
                "language": "French",
                "services": "",
                "source": "ODBus",
                "naics": "2211",
            },
            {
                "name": "Quebec Grid Engineering Partners",
                "industry": "Energy",
                "subsector": "Engineering",
                "country": "Canada",
                "province": "Quebec",
                "region": "North America",
                "city": "Quebec City",
                "language": "French",
                "services": "",
                "source": "ODBus",
                "naics": "5413",
            },
        ]
    )
