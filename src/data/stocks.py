import os
import glob
from src.data import alpha_vantage_api
import pandas as pd
from datetime import date


def get_weekly_data(
    symbol: str, api_key: str, files_dir: str = "securities"
) -> pd.DataFrame:
    """Gets the historical data of the given symbol in a DataFrame.
    """

    if not os.path.exists(files_dir):
        os.mkdir(files_dir)
    file_card = f"*{symbol}.csv"
    target_path = os.path.join(files_dir, file_card)
    files_found = glob.glob(target_path)
    if len(files_found) == 0:
        data = alpha_vantage_api.get_weekly_data(symbol=symbol, api_key=api_key)
        data.to_csv(f"{files_dir}/{date.today()}-{symbol}.csv")
    elif len(files_found) == 1:
        data = pd.read_csv(files_found[0], index_col=0)

    return data
