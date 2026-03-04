import os
import pandas as pd
from datetime import datetime, timezone

LOG_PATH = "data/signals_log.csv"

HISTORY_COLUMNS = [
    "run_date",
    "name",
    "industry",
    "province",
    "source",
    "lead_score",
    "growth_signal",
    "context",
    "opportunity"
]


def utc_date_iso() -> str:
    # Use UTC date for consistent nightly logging
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def append_signals_log(df: pd.DataFrame, run_date: str | None = None) -> pd.DataFrame:
    """
    Appends a nightly snapshot of key signals into data/signals_log.csv.
    Returns the full log dataframe.
    """
    run_date = run_date or utc_date_iso()

    snap = df.copy()
    snap["run_date"] = run_date

    # Ensure required columns exist
    for col in HISTORY_COLUMNS:
        if col not in snap.columns:
            snap[col] = ""

    snap = snap[HISTORY_COLUMNS].copy()

    if os.path.exists(LOG_PATH):
        existing = pd.read_csv(LOG_PATH)
        full = pd.concat([existing, snap], ignore_index=True)
    else:
        full = snap

    # Deduplicate identical snapshots for the same company and date
    full.drop_duplicates(subset=["run_date", "name"], inplace=True)

    os.makedirs("data", exist_ok=True)
    full.to_csv(LOG_PATH, index=False)
    return full


def load_signals_log() -> pd.DataFrame:
    if os.path.exists(LOG_PATH):
        return pd.read_csv(LOG_PATH)
    return pd.DataFrame(columns=HISTORY_COLUMNS)


def company_timeline(log_df: pd.DataFrame, company_name: str) -> pd.DataFrame:
    df = log_df[log_df["name"] == company_name].copy()
    if df.empty:
        return df
    df["run_date"] = pd.to_datetime(df["run_date"], errors="coerce")
    df = df.sort_values("run_date")
    return df
