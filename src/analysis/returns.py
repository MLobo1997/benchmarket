from datetime import datetime
import pandas as pd
from src.data import column_names
from src.data import stocks


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


def compare_stocks(
    baseline_symbol: str,
    targets_symbols: list,
    minimum_nr_of_months: int,
    subtract_returns_to_baseline: bool,
    api_key: str,
    growth_col: str = "growth",
) -> tuple:
    baseline_data = stocks.get_historical_data(baseline_symbol, api_key=api_key)
    targets_data = [
        stocks.get_historical_data(symbol, api_key=api_key)
        for symbol in targets_symbols
    ]
    min_date = baseline_data.index[-1]
    for data in targets_data:
        date = data.index[-1]
        if date > min_date:
            min_date = date

    filter_indexes = baseline_data.index >= min_date
    baseline_data = baseline_data[filter_indexes]

    for idx in range(len(targets_data)):
        filter_indexes = targets_data[idx].index >= min_date
        targets_data[idx] = targets_data[idx][filter_indexes]

    baseline_returns = (
        get_returns_by_year(baseline_data, minimum_nr_of_months=minimum_nr_of_months),
        get_continuous_return(baseline_data)["return"],
    )

    targets_returns = [
        (
            symbol,
            get_returns_by_year(data, minimum_nr_of_months=minimum_nr_of_months),
            get_continuous_return(data)["return"],
        )
        for symbol, data in zip(targets_symbols, targets_data)
    ]
    targets_returns.sort(key=lambda tup: tup[2], reverse=True)

    continuous_returns = {}
    continuous_returns["baseline"] = baseline_returns[1]
    continuous_returns["targets"] = [(x[0], x[2]) for x in targets_returns]

    returns_by_year = pd.DataFrame(
        columns=[baseline_symbol] + [target[0] for target in targets_returns]
    )

    for year, row in baseline_returns[0].iterrows():
        baseline_growth = row[growth_col]
        returns_by_year.loc[year, baseline_symbol] = baseline_growth
        for target in targets_returns:
            growth = target[1].loc[year, growth_col]
            if subtract_returns_to_baseline:
                growth = growth - baseline_growth
            returns_by_year.loc[year, target[0]] = growth

    median_yearly_returns = []
    avg_yearly_returns = []
    beat_the_market_ratios = []
    for column in returns_by_year.iloc[:, 1:]:
        median_yearly_returns.append((column, returns_by_year[column].median()))
        avg_yearly_returns.append((column, returns_by_year[column].mean()))
        beat_the_market_ratios.append((column, (returns_by_year[column] >= 0).mean()))
    median_yearly_returns.sort(key=lambda x: x[1], reverse=True)
    avg_yearly_returns.sort(key=lambda x: x[1], reverse=True)
    beat_the_market_ratios.sort(key=lambda x: x[1], reverse=True)

    return (
        continuous_returns,
        returns_by_year,
        median_yearly_returns,
        avg_yearly_returns,
        beat_the_market_ratios,
    )
