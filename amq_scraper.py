import pandas as pd


def scrape_amq():
    """Sample industrial signal feed representing companies discovered via AMQ."""

    data = [
        {
            "name": "Norda Stelo",
            "industry": "Engineering",
            "region": "Quebec",
            "country": "Canada",
            "source": "AMQ",
        },
        {
            "name": "Osisko Mining",
            "industry": "Mining",
            "region": "Quebec",
            "country": "Canada",
            "source": "AMQ",
        },
        {
            "name": "Vale Indonesia Growth Program",
            "industry": "Mining",
            "region": "Sulawesi",
            "country": "Indonesia",
            "source": "AMQ",
        },
        {
            "name": "Siemens Grid Modernization",
            "industry": "Energy",
            "region": "Bavaria",
            "country": "Germany",
            "source": "AMQ",
        },
    ]

    return pd.DataFrame(data)
