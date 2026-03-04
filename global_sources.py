import pandas as pd


REGIONAL_TARGETS = {
    "North America": 300,
    "Europe": 300,
    "Asia-Pacific": 200,
    "Middle East": 100,
    "Latin America": 100,
}


def scrape_global_energy():
    companies = [
        {
            "name": "NextEra Energy",
            "industry": "Energy",
            "subsector": "Renewables",
            "country": "USA",
            "province": "Florida",
            "region": "North America",
            "source": "EnergyRegistry",
        },
        {
            "name": "Ørsted",
            "industry": "Energy",
            "subsector": "Wind",
            "country": "Denmark",
            "province": "Capital Region",
            "region": "Europe",
            "source": "EnergyRegistry",
        },
        {
            "name": "Iberdrola Innovation Hub",
            "industry": "Energy",
            "subsector": "Grid",
            "country": "Spain",
            "province": "Basque Country",
            "region": "Europe",
            "source": "AssociationFeed",
        },
        {
            "name": "ACWA Power",
            "industry": "Infrastructure",
            "subsector": "Utilities",
            "country": "Saudi Arabia",
            "province": "Riyadh",
            "region": "Middle East",
            "source": "GovDataset",
        },
    ]

    return pd.DataFrame(companies)
