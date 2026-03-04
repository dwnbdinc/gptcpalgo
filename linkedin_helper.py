def linkedin_search_links(company):
    base = "https://www.linkedin.com/search/results/people/?keywords="

    roles = [
        "business development",
        "partnerships",
        "procurement",
        "operations"
    ]

    links = []

    for r in roles:
        query = f"{r} {company}"
        links.append(base + query.replace(" ", "%20"))

    return links
