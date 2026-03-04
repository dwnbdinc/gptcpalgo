def opportunity_angle(row):

    if row["industry"]=="Mining":
        return "Remote logistics or operational partnership"

    if row["industry"]=="Energy":
        return "Infrastructure collaboration opportunity"

    return "General partnership exploration"
