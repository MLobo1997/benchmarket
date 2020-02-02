from datetime import datetime
import pandas as pd


def return_by_year(
    data: pd.DataFrame,
    minimum_nr_of_weeks: int = None,
    open_col: str = "open",
    close_col: str = "close",
    growth_col: str = "growth (%)",
) -> pd.DataFrame:
    """Returns a dataframe representing the returns of a stock year by year.

    Parameters
    ----------
    minimum_nr_of_weeks: The minimum number of weeks present in the data to display a year. If None, all years will be displayed
    """
    minimum_nr_of_weeks = None
    open_col = "open"
    close_col = "close"
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
    result[growth_col] = 100 * (result[close_col] - result[open_col]) / result[open_col]
    return result
