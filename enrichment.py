def enrich(df):

    df["domain_guess"] = (
        df["name"].str.lower().str.replace(" ","") + ".com"
    )

    df["language"] = "French"

    return df
