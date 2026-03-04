import pandas as pd


def heating_up_accounts(log_df: pd.DataFrame, top_n: int = 25) -> pd.DataFrame:
    """
    Finds accounts with biggest positive change since the previous snapshot.
    Uses last two run_dates in the log.
    """
    if log_df.empty:
        return pd.DataFrame()

    # Normalize dates
    tmp = log_df.copy()
    tmp["run_date"] = pd.to_datetime(tmp["run_date"], errors="coerce")
    tmp = tmp.dropna(subset=["run_date"])

    if tmp["run_date"].nunique() < 2:
        return pd.DataFrame()

    last_date = tmp["run_date"].max()
    prev_date = sorted(tmp["run_date"].unique())[-2]

    last = tmp[tmp["run_date"] == last_date].copy()
    prev = tmp[tmp["run_date"] == prev_date].copy()

    # Keep latest values per company per day
    last = last.sort_values("run_date").drop_duplicates(subset=["name"], keep="last")
    prev = prev.sort_values("run_date").drop_duplicates(subset=["name"], keep="last")

    merged = last.merge(
        prev[["name", "lead_score", "growth_signal"]],
        on="name",
        how="left",
        suffixes=("", "_prev")
    )

    merged["lead_score_prev"] = merged["lead_score_prev"].fillna(0)
    merged["growth_signal_prev"] = merged["growth_signal_prev"].fillna(0)

    merged["delta_score"] = merged["lead_score"] - merged["lead_score_prev"]
    merged["delta_growth"] = merged["growth_signal"] - merged["growth_signal_prev"]

    merged = merged.sort_values(
        ["delta_score", "delta_growth", "lead_score"],
        ascending=False
    )

    cols = [
        "name", "industry", "province", "source",
        "lead_score", "delta_score",
        "growth_signal", "delta_growth",
        "opportunity", "context"
    ]
    cols = [c for c in cols if c in merged.columns]
    return merged.head(top_n)[cols].copy()
