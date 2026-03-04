import pandas as pd


def scrape_seao():
    """Sample procurement signal feed representing tenders and public bids."""

    tenders = [
        {
            "name": "Hydro Infrastructure Upgrade",
            "industry": "Energy",
            "subsector": "Hydro",
            "country": "Canada",
            "province": "Quebec",
            "region": "North America",
            "source": "SEAO",
        },
        {
            "name": "Santos Basin Offshore Construction",
            "industry": "Energy",
            "subsector": "Offshore",
            "country": "Brazil",
            "province": "Rio de Janeiro",
            "region": "Latin America",
            "source": "SEAO",
        },
        {
            "name": "Pilbara Autonomous Mine Expansion",
            "industry": "Mining",
            "subsector": "Iron Ore",
            "country": "Australia",
            "province": "Western Australia",
            "region": "Asia-Pacific",
            "source": "SEAO",
        },
    ]

    return pd.DataFrame(tenders)
