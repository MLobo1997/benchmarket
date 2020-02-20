from datetime import datetime
import pandas as pd
from src.data import column_names


def compute_return(open_value, close_value, in_percentage):
    growth = (close_value - open_value) / open_value
    if in_percentage:
        growth = 100 * growth
    return growth


def get_returns_by_year(
    data: pd.DataFrame,
    minimum_nr_of_months: int = None,
    in_percentage: bool = False,
    open_col: str = column_names.ADJ_OPEN_COL,
    close_col: str = column_names.ADJ_CLOSE_COL,
    growth_col: str = "growth",
) -> pd.DataFrame:
    """Returns a dataframe representing the returns of a stock year by year.

    Parameters
    ----------
    minimum_nr_of_months: The minimum number of months present in the data to display a year. If None, all years will be displayed
    """
    if minimum_nr_of_months is not None:
        year_list = []
        month_list = []
        for date in data.index:
            date_inst = datetime.strptime(date, "%Y-%m-%d")
            year_list.append(date_inst.year)
            month_list.append(date_inst.month)

        tmp = pd.DataFrame()
        tmp["year"] = year_list
        tmp["month"] = month_list
        months_per_year = tmp.groupby("year").month.nunique()
        year_is_valid = months_per_year >= minimum_nr_of_months
    result = pd.DataFrame(columns=[open_col, close_col])
    current_year = None
    previous_open_val = None
    for date, row in data.iterrows():
        open_val = row[open_col]
        close_val = row[close_col]
        dt = datetime.strptime(date, "%Y-%m-%d")
        if minimum_nr_of_months is not None and not year_is_valid[dt.year]:
            continue
        if current_year is None or dt.year < current_year:
            result.loc[dt.year, close_col] = close_val
            if previous_open_val is not None:
                result.loc[current_year, open_col] = previous_open_val
            current_year = dt.year
        previous_open_val = open_val
    result.loc[current_year, open_col] = previous_open_val
    result[growth_col] = compute_return(
        open_value=result[open_col],
        close_value=result[close_col],
        in_percentage=in_percentage,
    )
    return result


def get_continuous_return(
    data: pd.DataFrame,
    from_datetime: datetime = None,
    until_datetime: datetime = None,
    in_percentage: bool = False,
    open_col: str = column_names.ADJ_OPEN_COL,
    close_col: str = column_names.ADJ_CLOSE_COL,
    dividend_col: str = column_names.DIV_COL,
) -> dict:
    """Returns a dict with the growth returns, the dividend returns/amount and the total returns.
    """
    result = {}
    result[close_col] = None
    dividend_key = "total " + dividend_col
    result[dividend_key] = 0
    for date, row in data.iterrows():
        open_value = row[open_col]
        close_value = row[close_col]
        dividend = row[dividend_col]
        dt = datetime.strptime(date, "%Y-%m-%d")
        if until_datetime is not None and dt > until_datetime:
            continue
        if result[close_col] is None:
            result[close_col] = close_value
        if from_datetime is not None and dt < from_datetime:
            print(dt)
            break
        result[open_col] = open_value
        result[dividend_key] += dividend
        result["return"] = compute_return(
            open_value=result[open_col],
            close_value=result[close_col],
            in_percentage=in_percentage,
        )
    return result
