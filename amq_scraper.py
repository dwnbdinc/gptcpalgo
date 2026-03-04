import pandas as pd


def scrape_amq():
    """Sample industrial signal feed representing companies discovered via AMQ."""

    data = [
        {
            "name": "Norda Stelo",
            "industry": "Engineering",
            "subsector": "Consulting",
            "country": "Canada",
            "province": "Quebec",
            "region": "North America",
            "source": "AMQ",
        },
        {
            "name": "Osisko Mining",
            "industry": "Mining",
            "subsector": "Gold",
            "country": "Canada",
            "province": "Quebec",
            "region": "North America",
            "source": "AMQ",
        },
        {
            "name": "Vale Indonesia Growth Program",
            "industry": "Mining",
            "subsector": "Nickel",
            "country": "Indonesia",
            "province": "Sulawesi",
            "region": "Asia-Pacific",
            "source": "AMQ",
        },
        {
            "name": "Siemens Grid Modernization",
            "industry": "Energy",
            "subsector": "Grid",
            "country": "Germany",
            "province": "Bavaria",
            "region": "Europe",
            "source": "AMQ",
        },
    ]

    return pd.DataFrame(data)
