def score(df):

    def calc(row):
        s = 0

        if row["industry"] in ["Mining","Energy"]:
            s += 25

        if row["province"]=="Quebec":
            s += 10

        s += row["growth_signal"] * 10
        return s

    df["lead_score"] = df.apply(calc,axis=1)

    return df
