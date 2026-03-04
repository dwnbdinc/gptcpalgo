def detect_opportunities(df):
    events = []

    for _, row in df.iterrows():
        score = 0
        reasons = []

        if row["growth_signal"] >= 3:
            score += 2
            reasons.append("Expansion signals")

        if row["source"] == "SEAO":
            score += 2
            reasons.append("Active procurement")

        if row["industry"] in {"Mining", "Energy"}:
            score += 1
            reasons.append("Priority industry")

        if row["lead_score"] >= 55:
            score += 1
            reasons.append("High lead score")

        if score >= 3:
            events.append(
                {
                    "company": row["name"],
                    "industry": row["industry"],
                    "country": row["country"],
                    "province": row["province"],
                    "region": row["region"],
                    "confidence": "HIGH" if score >= 4 else "MEDIUM",
                    "reasons": ", ".join(reasons),
                    "opportunity": row["opportunity"],
                }
            )

    return events
