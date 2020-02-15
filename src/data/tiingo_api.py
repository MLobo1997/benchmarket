import requests
import pandas as pd
from datetime import datetime
from src.data import column_names


class ApiException(Exception):
    def __init__(self, message: str):
        self.message = message


column_names_map = {
    "close": column_names.CLOSE_COL,
    "high": column_names.HIGH_COL,
    "low": column_names.LOW_COL,
    "open": column_names.OPEN_COL,
    "volume": column_names.VOL_COL,
    "adjClose": column_names.ADJ_CLOSE_COL,
    "adjHigh": column_names.ADJ_HIGH_COL,
    "adjLow": column_names.ADJ_LOW_COL,
    "adjOpen": column_names.ADJ_OPEN_COL,
    "adjVolume": column_names.ADJ_VOL_COL,
    "divCash": column_names.DIV_COL,
}

URL_FORMAT = "https://api.tiingo.com/tiingo/daily/{symbol}/prices/prices?startDate={startDate}&endDate={endDate}"


def get_historical_data(
    symbol: str,
    api_key: str,
    startDate: datetime = datetime(1990, 1, 1),
    endDate: datetime = datetime.now(),
) -> pd.DataFrame:
    """Gets weekly aggregated data from the stock represented by the symbol. Returns a dataframe.
    """
    global URL_FORMAT

    url = URL_FORMAT.format(
        symbol=symbol,
        startDate=startDate.strftime("%Y-%m-%d"),
        endDate=endDate.strftime("%Y-%m-%d"),
    )
    headers = {"Content-type": "application/json", "Authorization": f"Token {api_key}"}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    if response.status_code != 200 or "Error Message" in response_json:
        raise ApiException(message=str(response_json))
    data_dict = {entry["date"][:10]: entry for entry in response_json}
    data = (
        pd.DataFrame(data_dict)
        .drop(axis=0, index="date")
        .transpose()
        .rename(mapper=column_names_map, axis=1)
    )
    return data
