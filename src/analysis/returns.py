from datetime import datetime
import pandas as pd


def compute_return(open_value, close_value, in_percentage):
    growth = (close_value - open_value) / open_value
    if in_percentage:
        growth = 100 * growth
    return growth


def analyze_returns(
    data: pd.DataFrame,
    minimum_nr_of_weeks: int = None,
    in_percentage: bool = False,
    open_col: str = "open",
    close_col: str = "close",
    growth_col: str = "growth",
) -> pd.DataFrame:
    """Returns a dataframe representing the returns of a stock year by year.

    Parameters
    ----------
    minimum_nr_of_weeks: The minimum number of weeks present in the data to display a year. If None, all years will be displayed
    """
    if minimum_nr_of_weeks is not None:
        count_per_year = (
            data.iloc[:, 0]
            .groupby(lambda date: datetime.strptime(date, "%Y-%m-%d").year)
            .count()
        )
        year_is_valid = count_per_year >= minimum_nr_of_weeks
    result = pd.DataFrame(columns=[open_col, close_col])
    current_year = None
    previous_open_val = None
    for (date, open_val), close_val in zip(data[open_col].items(), data[close_col]):
        dt = datetime.strptime(date, "%Y-%m-%d")
        if minimum_nr_of_weeks is not None and not year_is_valid[dt.year]:
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
