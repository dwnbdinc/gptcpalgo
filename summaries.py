def generate_summary(row):

    return f"""
Company: {row['name']}
Industry: {row['industry']}
Lead Score: {row['lead_score']}

Context:
{row['context']}

Opportunity:
{row['opportunity']}
"""
