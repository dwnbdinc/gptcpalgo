PRIORITY_INDUSTRIES = {
    "Mining": 25,
    "Energy": 25,
    "Engineering": 10,
}

COUNTRY_STRATEGIC_WEIGHT = {
    "Canada": 10,
    "Australia": 8,
    "Brazil": 8,
    "Germany": 8,
    "Indonesia": 7,
}


def score(df):
    def calc(row):
        score_value = PRIORITY_INDUSTRIES.get(row["industry"], 0)
        score_value += COUNTRY_STRATEGIC_WEIGHT.get(row["country"], 5)
        score_value += row["growth_signal"] * 10
        return score_value

    df["lead_score"] = df.apply(calc, axis=1)
    return df
