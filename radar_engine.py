def detect_opportunities(df):

    events=[]

    for _,row in df.iterrows():

        score=0
        reasons=[]

        if row["growth_signal"]>=2:
            score+=2
            reasons.append("Expansion signals")

        if row["source"]=="SEAO":
            score+=2
            reasons.append("Active procurement")

        if row["industry"]=="Mining":
            score+=1
            reasons.append("Remote operations")

        if score>=3:
            events.append({
                "company":row["name"],
                "industry":row["industry"],
                "confidence":"HIGH",
                "reasons":", ".join(reasons),
                "opportunity":row["opportunity"]
            })

    return events
