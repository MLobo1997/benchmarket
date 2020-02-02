import requests
import pandas as pd


class ApiException(Exception):
    def __init__(self, message: str):
        self.message = message


URL_FORMAT = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={api_key}"


def get_weekly_data(symbol: str, api_key: str) -> pd.DataFrame:
    """Gets weekly aggregated data from the stock represented by the symbol. Returns a dataframe.
    """
    global URL_FORMAT

    url = URL_FORMAT.format(symbol=symbol, api_key=api_key)
    response = requests.get(url)
    response_json = response.json()
    if response.status_code != 200 or "Error Message" in response_json:
        raise ApiException(message=str(response_json))
    data = (
        pd.DataFrame(response.json()["Weekly Adjusted Time Series"])
        .astype(float)
        .transpose()
        .rename(mapper=lambda x: x[3:], axis=1)  # standardizes column names
    )

    return data
