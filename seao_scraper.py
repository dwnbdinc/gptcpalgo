import pandas as pd


def scrape_seao():
    """Sample procurement signal feed representing tenders and public bids."""

    tenders = [
        {
            "name": "Hydro Infrastructure Upgrade",
            "industry": "Energy",
            "region": "Quebec",
            "country": "Canada",
            "source": "SEAO",
        },
        {
            "name": "Santos Basin Offshore Construction",
            "industry": "Energy",
            "region": "Rio de Janeiro",
            "country": "Brazil",
            "source": "SEAO",
        },
        {
            "name": "Pilbara Autonomous Mine Expansion",
            "industry": "Mining",
            "region": "Western Australia",
            "country": "Australia",
            "source": "SEAO",
        },
    ]

    return pd.DataFrame(tenders)
