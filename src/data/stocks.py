import os
import glob
from src.data import alpha_vantage_api, tiingo_api
import pandas as pd
from datetime import date


def get_historical_data(
    symbol: str, api_key: str, files_dir: str = "securities", which_api: str = "tiingo"
) -> pd.DataFrame:
    """Gets the historical data of the given symbol in a DataFrame.
    """

    assert which_api in ["tiingo", "alpha_vantage"]

    if not os.path.exists(files_dir):
        os.mkdir(files_dir)
    file_card = f"*-{symbol}.csv"
    target_path = os.path.join(files_dir, file_card)
    files_found = glob.glob(target_path)
    if len(files_found) == 0:
        if which_api == "alpha_vantage":
            data = alpha_vantage_api.get_weekly_data(symbol=symbol, api_key=api_key)
        elif which_api == "tiingo":
            data = tiingo_api.get_historical_data(symbol=symbol, api_key=api_key)

        data.to_csv(f"{files_dir}/{date.today()}-{symbol}.csv")
    elif len(files_found) == 1:
        data = pd.read_csv(files_found[0], index_col=0)
    else:
        print(files_found)

    return data
