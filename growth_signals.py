def detect_growth(df):

    df["growth_signal"] = 0

    df.loc[df["source"]=="SEAO","growth_signal"] += 3

    keywords = ["project","energy","mine","construction"]

    for k in keywords:
        df.loc[df["name"].str.contains(k,case=False,na=False),"growth_signal"] += 1

    return df
