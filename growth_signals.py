SOURCE_SIGNAL_WEIGHT = {
    "SEAO": 3,
    "AMQ": 1,
}


def detect_growth(df):
    df["growth_signal"] = 0

    for source, weight in SOURCE_SIGNAL_WEIGHT.items():
        df.loc[df["source"] == source, "growth_signal"] += weight

    keywords = [
        "project",
        "energy",
        "mine",
        "construction",
        "upgrade",
        "expansion",
        "modernization",
        "infrastructure",
    ]

    for keyword in keywords:
        df.loc[df["name"].str.contains(keyword, case=False, na=False), "growth_signal"] += 1

    return df
