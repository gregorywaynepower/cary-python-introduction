import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Cleaning Data

        ## About the data
        In this notebook, we will using daily temperature data from the [National Centers for Environmental Information (NCEI) API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2). We will use the Global Historical Climatology Network - Daily (GHCND) dataset; see the documentation [here](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf).

        This data was collected from the LaGuardia Airport station in New York City for October 2018. It contains:
        - the daily minimum temperature (`TMIN`)
        - the daily maximum temperature (`TMAX`)
        - the daily average temperature (`TAVG`)

        *Note: The NCEI is part of the National Oceanic and Atmospheric Administration (NOAA) and, as you can see from the URL for the API, this resource was created when the NCEI was called the NCDC. Should the URL for this resource change in the future, you can search for "NCEI weather API" to find the updated one.*

        In addition, we will be using S&P 500 stock market data (obtained using the [`stock_analysis`](https://github.com/stefmolin/stock-analysis) package and data for bitcoin for 2017 through 2018. For the first edition, the bitcoin data was collected from CoinMarketCap using the `stock_analysis` package; however, changes in the website led to the necessity of changing the data source to Yahoo! Finance. The bitcoin data that was collected before the CoinMarketCap website change should be equivalent to the historical data that can be viewed on [this](https://coinmarketcap.com/currencies/bitcoin/historical-data/) page.

        ## Setup
        We need to import `pandas` and read in the temperature data to get started:
        """
    )
    return


@app.cell
def _():
    import pandas as pd

    df = pd.read_csv('../data/nyc_temperatures.csv')
    df.head()
    return df, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Renaming Columns
        We start out with the following columns:
        """
    )
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We want to rename the `value` column to indicate it contains the temperature in Celsius and the `attributes` column to say `flags` since each value in the comma-delimited string is a different flag about the data collection. For this task, we use the `rename()` method and pass in a dictionary mapping the column names to their new names. We pass `inplace=True` to change our original dataframe instead of getting a new one back:
        """
    )
    return


@app.cell
def _(df):
    df.rename(
        columns={
            'value': 'temp_C',
            'attributes': 'flags'
        }, inplace=True
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Those columns have been successfully renamed:
        """
    )
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also perform string operations on the column names with `rename()`:
        """
    )
    return


@app.cell
def _(df):
    df.rename(str.upper, axis='columns').columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Type Conversion
        The `date` column is not currently being stored as a `datetime`:
        """
    )
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's perform the conversion with `pd.to_datetime()`:
        """
    )
    return


@app.cell
def _(df, pd):
    df.loc[:,'date'] = pd.to_datetime(df.date)
    df.dtypes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now we get useful information when we use `describe()` on this column:
        """
    )
    return


@app.cell
def _(df):
    df.date.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can use `tz_localize()` on a `DatetimeIndex` object to convert to a desired timezone:
        """
    )
    return


@app.cell
def _(pd):
    pd.date_range(start='2018-10-25', periods=2, freq='D').tz_localize('EST')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This also works with `Series`/`DataFrame` objects that have an index of type `DatetimeIndex`. Let's read in the CSV again for this example and set the `date` column to be the index and stored as a datetime:
        """
    )
    return


@app.cell
def _(pd):
    eastern = pd.read_csv(
        '../data/nyc_temperatures.csv', index_col='date', parse_dates=True
    ).tz_localize('EST')
    eastern.head()
    return (eastern,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can use `tz_convert()` to convert to another timezone from there. If we convert the Eastern datetimes to UTC, they will now be at 5 AM, since `pandas` will use the offsets to convert:
        """
    )
    return


@app.cell
def _(eastern):
    eastern.tz_convert('UTC').head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can change the period of the index as well. We could change the period to be monthly to make it easier to aggregate later.

        The reason we have to add the parameter within `tz_localize()` to `None` for this, is because we'll get a warning from `pandas` that our output class `PeriodArray` doesn't have time zone information and we'll lose it.
        """
    )
    return


@app.cell
def _(eastern):
    eastern.tz_localize(None).to_period('M').index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We now get a `PeriodIndex` object, which we can change back into a `DatetimeIndex` object with `to_timestamp()`:
        """
    )
    return


@app.cell
def _(eastern):
    eastern.tz_localize(None).to_period('M').to_timestamp().index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can use the `assign()` method for working with multiple columns at once (or creating new ones). Since our `date` column has already been converted, we need to read in the data again:
        """
    )
    return


@app.cell
def _(pd):
    df_1 = pd.read_csv('../data/nyc_temperatures.csv').rename(columns={'value': 'temp_C', 'attributes': 'flags'})
    new_df = df_1.assign(date=pd.to_datetime(df_1.date), temp_F=df_1.temp_C * 9 / 5 + 32)
    new_df.dtypes
    return df_1, new_df


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `date` column now has datetimes and the `temp_F` column was added:
        """
    )
    return


@app.cell
def _(new_df):
    new_df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also use `astype()` to perform conversions. Let's create columns of the integer portion of the temperatures in Celsius and Fahrenheit. We will use **lambda functions** (first introduced in *Chapter 2, Working with Pandas DataFrames*), so that we can use the values being created in the `temp_F` column to calculate the `temp_F_whole` column. It is very common (and useful) to use lambda functions with `assign()`:
        """
    )
    return


@app.cell
def _(df_1, pd):
    df_2 = df_1.assign(date=lambda x: pd.to_datetime(x.date), temp_C_whole=lambda x: x.temp_C.astype('int'), temp_F=lambda x: x.temp_C * 9 / 5 + 32, temp_F_whole=lambda x: x.temp_F.astype('int'))
    df_2.head()
    return (df_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Creating categories:
        """
    )
    return


@app.cell
def _(df_2):
    df_with_categories = df_2.assign(station=df_2.station.astype('category'), datatype=df_2.datatype.astype('category'))
    df_with_categories.dtypes
    return (df_with_categories,)


@app.cell
def _(df_with_categories):
    df_with_categories.describe(include='category')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Our categories have no order, but this is something that `pandas` supports:
        """
    )
    return


@app.cell
def _(pd):
    pd.Categorical(
        ['med', 'med', 'low', 'high'], 
        categories=['low', 'med', 'high'],
        ordered=True
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Reordering, reindexing, and sorting
        Say we want to find the days that reached the hottest temperatures in the weather data; we can sort our values by the `temp_C` column with the largest on top to find this: 
        """
    )
    return


@app.cell
def _(df_2):
    df_2[df_2.datatype == 'TMAX'].sort_values(by='temp_C', ascending=False).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, this isn't perfect because we have some ties, and they aren't sorted consistently. In the first tie between the 7th and the 10th, the earlier date comes first, but the opposite is true with the tie between the 4th and the 2nd. We can use other columns to break ties and specify how to sort each with `ascending`. Let's break ties with the date column and show earlier dates before later ones:
        """
    )
    return


@app.cell
def _(df_2):
    df_2[df_2.datatype == 'TMAX'].sort_values(by=['temp_C', 'date'], ascending=[False, True]).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Notice that the index was jumbled in the past 2 results. Here, our index only stores the row number in the original data, but we may not need to keep track of that information. In this case, we can pass in `ignore_index=True` to get a new index after sorting:
        """
    )
    return


@app.cell
def _(df_2):
    df_2[df_2.datatype == 'TMAX'].sort_values(by=['temp_C', 'date'], ascending=[False, True], ignore_index=True).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When just looking for the n-largest values, rather than wanting to sort all the data, we can use `nlargest()`:
        """
    )
    return


@app.cell
def _(df_2):
    df_2[df_2.datatype == 'TAVG'].nlargest(n=10, columns='temp_C')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We use `nsmallest()` for the n-smallest values.
        """
    )
    return


@app.cell
def _(df_2):
    df_2.nsmallest(n=5, columns=['temp_C', 'date'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `sample()` method will give us rows (or columns with `axis=1`) at random. We can provide a seed (`random_state`) to make this reproducible. The index after we do this is jumbled:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.sample(5, random_state=0).index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can use `sort_index()` to order it again:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.sample(5, random_state=0).sort_index().index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `sort_index()` method can also sort columns alphabetically:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.sort_index(axis=1).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This can make selection with `loc` easier for many columns:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.sort_index(axis=1).head().loc[:, 'temp_C':'temp_F_whole']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We must sort the index to compare two dataframes. If the index is different, but the data is the same, they will be marked not-equal:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.equals(df_2.sort_values(by='temp_C'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Sorting the index solves this issue:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.equals(df_2.sort_values(by='temp_C').sort_index())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's set the `date` column as our index:
        """
    )
    return


@app.cell
def _(df_2):
    df_2.set_index('date', inplace=True)
    df_2.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now that we have an index of type `DatetimeIndex`, we can do datetime slicing and indexing. As long as we provide a date format that pandas understands, we can grab the data. To select all of 2018, we simply use `df.loc['2018']`, for the fourth quarter of 2018 we can use `df.loc['2018-Q4']`, grabbing October is as simple as using `df.loc['2018-10']`; these can also be combined to build ranges. Let's grab October 11, 2018 through October 12, 2018 (inclusive of both endpoints)&mdash;note that using `loc[]` is optional for ranges:
        """
    )
    return


@app.cell
def _(df_2):
    df_2['2018-10-11':'2018-10-12']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also use `reset_index()` to get a fresh index and move our current index into a column for safe keeping. This is especially useful if we had data, such as the date, in the index that we don't want to lose:
        """
    )
    return


@app.cell
def _(df_2):
    df_2['2018-10-11':'2018-10-12'].reset_index()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Reindexing allows us to conform our axis to contain a given set of labels. Let's turn to the S&P 500 stock data in the `sp500.csv` file to see an example of this. Notice we only have data for trading days (weekdays, excluding holidays):
        """
    )
    return


@app.cell
def _(pd):
    sp = pd.read_csv(
        '../data/sp500.csv', index_col='date', parse_dates=True
    ).drop(columns=['adj_close'])

    sp.head(10).assign(
        day_of_week=lambda x: x.index.day_name()
    )
    return (sp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If we want to look at the value of a portfolio (group of assets) that trade on different days, we need to handle the mismatch in the index. Bitcoin, for example, trades daily. If we sum up all the data we have for each day (aggregations will be covered in chapter 4, so don't fixate on this part), we get the following:
        """
    )
    return


@app.cell
def _(pd, sp):
    bitcoin = pd.read_csv(
        '../data/bitcoin.csv', index_col='date', parse_dates=True
    ).drop(columns=['market_cap'])

    # every day's closing price = S&P 500 close + Bitcoin close (same for other metrics)
    portfolio = pd.concat([sp, bitcoin], sort=False).groupby(level='date').sum()

    portfolio.head(10).assign(
        day_of_week=lambda x: x.index.day_name()
    )
    return bitcoin, portfolio


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It may not be immediately obvious what is wrong with the previous data, but with a visualization we can easily see the cyclical pattern of drops on the days the stock market is closed. (Don't worry about the plotting code too much, we will cover it in depth in chapters 5 and 6).

        We will need to import `matplotlib` now:
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt # we use this module for plotting
    from matplotlib.ticker import StrMethodFormatter # for formatting the axis
    return StrMethodFormatter, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now we can see why we need to reindex:
        """
    )
    return


@app.cell
def _(StrMethodFormatter, plt, portfolio):
    _ax = portfolio['2017-Q4':'2018-Q2'].plot(y='close', figsize=(15, 5), legend=False, title='Bitcoin + S&P 500 value without accounting for different indices')
    _ax.set_ylabel('price')
    _ax.yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
    for _spine in ['top', 'right']:
        _ax.spines[_spine].set_visible(False)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We need to align the index of the S&P 500 to match bitcoin in order to fix this. We will use the `reindex()` method, but by default we get `NaN` for the values that we don't have data for:
        """
    )
    return


@app.cell
def _(bitcoin, sp):
    sp.reindex(bitcoin.index).head(10).assign(
        day_of_week=lambda x: x.index.day_name()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So now we have rows for every day of the year, but all the weekends and holidays have `NaN` values. To address this, we can specify how to handle missing values with the `method` argument. In this case, we want to forward-fill, which will put the weekend and holiday values as the value they had for the Friday (or end of trading week) before:
        """
    )
    return


@app.cell
def _(bitcoin, sp):
    sp.reindex(bitcoin.index, method='ffill').head(10)\
        .assign(day_of_week=lambda x: x.index.day_name())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To isolate the changes happening with the forward-filling, we can use the `compare()` method. It shows us the values that differ across identically-labeled dataframes (same names and same columns). Here, we can see that only weekends and holidays (Monday, January 16, 2017 was MLK day) have values forward-filled. Notice that consecutive days have the same values.
        """
    )
    return


@app.cell
def _(bitcoin, sp):
    sp.reindex(bitcoin.index)\
        .compare(sp.reindex(bitcoin.index, method='ffill'))\
        .head(10).assign(day_of_week=lambda x: x.index.day_name())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This isn't perfect though. We probably want 0 for the volume traded and to put the closing price for the open, high, low, and close on the days the market is closed:

        The reason why we're using `np.where(boolean condition, value if True, value if False)` within `lambda` functions in the example below, is that <b>vectorized operations</b> allow us to be faster and more efficient than utilizing `for` loops to perform calculations on arrays all at once.
        """
    )
    return


@app.cell
def _(bitcoin, sp):
    import numpy as np

    sp_reindexed = sp.reindex(bitcoin.index).assign(
        volume=lambda x: x.volume.fillna(0), # put 0 when market is closed
        close=lambda x: x.close.fillna(method='ffill'), # carry this forward
        # take the closing price if these aren't available
        open=lambda x: np.where(x.open.isnull(), x.close, x.open),
        high=lambda x: np.where(x.high.isnull(), x.close, x.high),
        low=lambda x: np.where(x.low.isnull(), x.close, x.low)
    )
    sp_reindexed.head(10).assign(
        day_of_week=lambda x: x.index.day_name()
    )
    return (sp_reindexed,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If we create a visualization comparing the reindexed data to the first attempt, we see how reindexing helped maintain the asset value when the market was closed:
        """
    )
    return


@app.cell
def _(StrMethodFormatter, bitcoin, plt, portfolio, sp_reindexed):
    fixed_portfolio = sp_reindexed + bitcoin
    _ax = fixed_portfolio['2017-Q4':'2018-Q2'].plot(y='close', label='reindexed portfolio of S&P 500 + Bitcoin', figsize=(15, 5), linewidth=2, title='Reindexed portfolio vs. portfolio with mismatched indices')
    portfolio['2017-Q4':'2018-Q2'].plot(y='close', ax=_ax, linestyle='--', label='portfolio of S&P 500 + Bitcoin w/o reindexing')
    _ax.set_ylabel('price')
    _ax.yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
    for _spine in ['top', 'right']:
        _ax.spines[_spine].set_visible(False)
    plt.show()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
