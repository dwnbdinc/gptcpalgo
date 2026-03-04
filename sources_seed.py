import pandas as pd

from sources_common import normalize_company_df

SEED_PATH = "data/companies_seed_1000.csv"


def scrape_seed_global_1000() -> pd.DataFrame:
    df = pd.read_csv(SEED_PATH)
    return normalize_company_df(df, source_label="GlobalSeed")
