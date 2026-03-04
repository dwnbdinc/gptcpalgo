import pandas as pd

def scrape_amq():

    data = [
        {"name":"Norda Stelo","industry":"Engineering","province":"Quebec","source":"AMQ"},
        {"name":"Osisko Mining","industry":"Mining","province":"Quebec","source":"AMQ"},
    ]

    return pd.DataFrame(data)
