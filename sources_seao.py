import pandas as pd

from seao_scraper import scrape_seao
from sources_common import normalize_company_df


def scrape_seao_source() -> pd.DataFrame:
    df = scrape_seao()

    # Your SEAO ingestion may represent tenders rather than companies.
    # We treat them as buyer/opportunity entities for now, but keep schema consistent.
    if "industry" not in df.columns:
        df["industry"] = "Energy"
    if "province" not in df.columns:
        df["province"] = "Quebec"
    if "country" not in df.columns:
        df["country"] = "Canada"
    if "region" not in df.columns:
        df["region"] = "North America"
    if "subsector" not in df.columns:
        df["subsector"] = "Procurement"

    return normalize_company_df(df, source_label="SEAO")
