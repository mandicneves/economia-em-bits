import pandas as pd


def load_inflation_data() -> pd.DataFrame:
    import requests

    ipca_urls = {
        "total": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4449/dados?formato=json",
    }

    response = requests.get(ipca_urls["total"])
    data = response.json()

    return pd.DataFrame(data=data, columns=["data", "valor"])