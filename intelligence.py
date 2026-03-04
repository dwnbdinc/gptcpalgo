def build_context(row):
    context = []

    if row["industry"] == "Mining":
        context.append("Remote operations likely")

    if row["growth_signal"] > 2:
        context.append("Expansion phase detected")

    if row["source"] == "SEAO":
        context.append("Active procurement buyer")

    context.append(f"Geography: {row['region']}, {row['country']}")

    return ", ".join(context)
