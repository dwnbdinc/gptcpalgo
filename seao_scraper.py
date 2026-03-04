import pandas as pd

def scrape_seao():

    tenders = [
        {"name":"Hydro Infrastructure Upgrade","industry":"Energy","province":"Quebec","source":"SEAO"}
    ]

    return pd.DataFrame(tenders)
