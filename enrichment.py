LANGUAGE_BY_COUNTRY = {
    "Canada": "English/French",
    "Brazil": "Portuguese",
    "Germany": "German",
    "Australia": "English",
    "Indonesia": "Indonesian",
}


def enrich(df):
    df["domain_guess"] = df["name"].str.lower().str.replace(" ", "", regex=False) + ".com"
    df["language"] = df["country"].map(LANGUAGE_BY_COUNTRY).fillna("English")
    df["market_scope"] = "Global"
    return df
