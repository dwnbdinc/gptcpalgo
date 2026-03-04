import pandas as pd


def build_research_queue(df, limit=25):
    df = df.copy()

    df["queue_priority"] = (
        df["lead_score"]
        + (df["growth_signal"] * 5)
    )

    df = df.sort_values("queue_priority", ascending=False)

    queue = df.head(limit).copy()

    queue["research_status"] = "New"

    return queue
