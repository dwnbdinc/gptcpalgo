from __future__ import annotations

import pandas as pd

from sources_common import canonicalize_name
from sources_registry import get_sources


def collect_companies() -> pd.DataFrame:
    sources = [s for s in get_sources() if s.enabled]

    frames = []
    for s in sources:
        try:
            df = s.scraper()
            if df is None:
                continue
            df = df.copy()
            df["source_rank"] = s.rank
            df["source_key"] = s.key
            frames.append(df)
        except Exception:
            # Conservative: don’t fail the whole pipeline if a single source breaks
            # You can later log errors to a file.
            continue

    if not frames:
        return pd.DataFrame()

    df_all = pd.concat(frames, ignore_index=True)

    # Canonical name for dedupe
    df_all["name_norm"] = df_all["name"].apply(canonicalize_name)

    # Prefer best-ranked source (lowest rank)
    df_all = df_all.sort_values(["name_norm", "source_rank"], ascending=[True, True])

    # If you want to dedupe by (name,country) later, switch subset below
    df_all = df_all.drop_duplicates(subset=["name_norm"], keep="first")

    df_all = df_all.drop(columns=["name_norm"])

    return df_all
