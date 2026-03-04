import pandas as pd

from amq_scraper import scrape_amq
from sources_common import normalize_company_df


def scrape_amq_source() -> pd.DataFrame:
    df = scrape_amq()
    # Ensure at least name/industry/province/source exist
    if "industry" not in df.columns:
        df["industry"] = "Mining"
    if "province" not in df.columns:
        df["province"] = "Quebec"
    if "country" not in df.columns:
        df["country"] = "Canada"
    if "region" not in df.columns:
        df["region"] = "North America"
    if "subsector" not in df.columns:
        df["subsector"] = ""

    return normalize_company_df(df, source_label="AMQ")
