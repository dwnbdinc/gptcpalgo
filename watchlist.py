import pandas as pd

WATCHLIST_COLUMNS = ["name", "notes", "priority"]


def empty_watchlist() -> pd.DataFrame:
    return pd.DataFrame(columns=WATCHLIST_COLUMNS)


def load_watchlist_from_upload(uploaded_file) -> pd.DataFrame:
    if uploaded_file is None:
        return empty_watchlist()

    try:
        df = pd.read_csv(uploaded_file)
    except Exception:
        return empty_watchlist()

    # Normalize columns
    for col in WATCHLIST_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    df = df[WATCHLIST_COLUMNS].copy()
    df["name"] = df["name"].astype(str)
    return df


def apply_watchlist_filter(companies_df: pd.DataFrame, watchlist_df: pd.DataFrame) -> pd.DataFrame:
    if watchlist_df is None or watchlist_df.empty:
        return companies_df
    names = set(watchlist_df["name"].dropna().astype(str).tolist())
    return companies_df[companies_df["name"].astype(str).isin(names)].copy()
