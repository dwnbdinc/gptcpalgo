from __future__ import annotations

import pandas as pd

BASE_COLUMNS = [
    "name",
    "industry",
    "subsector",
    "country",
    "region",
    "province",
    "city",
    "language",
    "website",
    "domain_guess",
    "source",
]


def normalize_company_df(df: pd.DataFrame, source_label: str) -> pd.DataFrame:
    """
    Ensures a consistent schema across sources.
    """
    if df is None or df.empty:
        return pd.DataFrame(columns=BASE_COLUMNS)

    out = df.copy()

    # Create missing columns
    for col in BASE_COLUMNS:
        if col not in out.columns:
            out[col] = ""

    out["source"] = source_label
    out["name"] = out["name"].astype(str).str.strip()

    # Keep only base columns (you can extend later)
    out = out[BASE_COLUMNS].copy()

    # Remove empty names
    out = out[out["name"].astype(str).str.len() > 0].copy()

    return out


def canonicalize_name(name: str) -> str:
    s = str(name).lower().strip()
    # collapse whitespace
    s = " ".join(s.split())
    return s
