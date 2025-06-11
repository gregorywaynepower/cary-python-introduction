import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Handling duplicate, missing, or invalid data

    ## About the data
    In this notebook, we will using daily weather data that was taken from the [National Centers for Environmental Information (NCEI) API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) and altered to introduce many common problems faced when working with data. 

    *Note: The NCEI is part of the National Oceanic and Atmospheric Administration (NOAA) and, as you can see from the URL for the API, this resource was created when the NCEI was called the NCDC. Should the URL for this resource change in the future, you can search for "NCEI weather API" to find the updated one.*

    ## Background on the data

    Data meanings:
    - `PRCP`: precipitation in millimeters
    - `SNOW`: snowfall in millimeters
    - `SNWD`: snow depth in millimeters
    - `TMAX`: maximum daily temperature in Celsius
    - `TMIN`: minimum daily temperature in Celsius
    - `TOBS`: temperature at time of observation in Celsius
    - `WESF`: water equivalent of snow in millimeters

    Some important facts to get our bearings:
    - According to the National Weather Service, the coldest temperature ever recorded in Central Park was -15°F (-26.1°C) on February 9, 1934: [source](https://www.weather.gov/media/okx/Climate/CentralPark/extremes.pdf) 
    - The temperature of the Sun's photosphere is approximately 5,505°C: [source](https://en.wikipedia.org/wiki/Sun)

    ## Setup
    We need to import `pandas` and read in the dirty data to get started:
    """
    )
    return


@app.cell
def _():
    import pandas as pd

    df = pd.read_csv('data/dirty_data.csv')
    return df, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Finding problematic data
    A good first step is to look at some rows:
    """
    )
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Looking at summary statistics can reveal strange or missing values:""")
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The `info()` method can pinpoint missing values and wrong data types:""")
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can use the `isna()`/`isnull()` method of the series to find nulls:""")
    return


@app.cell
def _(df):
    contain_nulls = df[
        df.SNOW.isna() | df.SNWD.isna() | df.TOBS.isna()
        | df.WESF.isna() | df.inclement_weather.isna()
    ]
    contain_nulls.shape[0]
    return (contain_nulls,)


@app.cell
def _(contain_nulls):
    contain_nulls.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Note that we can't check if we have `NaN` like this:""")
    return


@app.cell
def _(df):
    df[df.inclement_weather == 'NaN'].shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This is because it is actually `np.nan`. However, notice this also doesn't work:""")
    return


@app.cell
def _(df):
    import numpy as np
    df[df.inclement_weather == np.nan].shape[0]
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We have to use one of the methods discussed earlier for this to work:""")
    return


@app.cell
def _(df):
    df[df.inclement_weather.isna()].shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can find `-inf`/`inf` by comparing to `-np.inf`/`np.inf`:""")
    return


@app.cell
def _(df, np):
    df[df.SNWD.isin([-np.inf, np.inf])].shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Rather than do this for each column, we can write a function that will use a [dictionary comprehension](https://www.python.org/dev/peps/pep-0274/) to check all the columns for us:""")
    return


@app.cell
def _(df, np):
    def get_inf_count(df):
        """Find the number of inf/-inf values per column in the dataframe"""
        return {
            col: df[df[col].isin([np.inf, -np.inf])].shape[0] for col in df.columns
        }

    get_inf_count(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Before we can decide how to handle the infinite values of snow depth, we should look at the summary statistics for snowfall, which forms a big part in determining the snow depth:""")
    return


@app.cell
def _(df, np, pd):
    pd.DataFrame({
        'np.inf Snow Depth': df[df.SNWD == np.inf].SNOW.describe(),
        '-np.inf Snow Depth': df[df.SNWD == -np.inf].SNOW.describe()
    }).T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's now look into the `date` and `station` columns. We saw the `?` for station earlier, so we know that was the other unique value. However, we see that some dates are present 8 times in the data and we only have 324 days meaning we are also missing days:""")
    return


@app.cell
def _(df):
    df.describe(include='object')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can use the `duplicated()` method to find duplicate rows:""")
    return


@app.cell
def _(df):
    df[df.duplicated()].shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The default for `keep` is `'first'` meaning it won't show the first row that the duplicated data was seen in; we can pass in `False` to see it though:""")
    return


@app.cell
def _(df):
    df[df.duplicated(keep=False)].shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can also specify the columns to use:""")
    return


@app.cell
def _(df):
    df[df.duplicated(['date', 'station'])].shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's look at a few duplicates. Just in the few values we see here, we know that the top 4 are actually in the data 6 times because by default we aren't seeing their first occurrence:""")
    return


@app.cell
def _(df):
    df[df.duplicated()].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Mitigating Issues

    ### Handling duplicated data
    Since we know we have NY weather data and noticed we only had two entries for `station`, we may decide to drop the `station` column because we are only interested in the weather data. However, when dealing with duplicate data, we need to think of the ramifications of removing it. Notice we only have data for the `WESF` column when the station is `?`:
    """
    )
    return


@app.cell
def _(df):
    df[df.WESF.notna()].station.unique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If we determine it won't impact our analysis, we can use `drop_duplicates()` to remove them:""")
    return


@app.cell
def _(df, pd):
    # 1. make the date a datetime
    df.date = pd.to_datetime(df.date)

    # 2. save this information for later
    station_qm_wesf = df[df.station == '?'].drop_duplicates('date').set_index('date').WESF

    # 3. sort ? to the bottom
    df.sort_values('station', ascending=False, inplace=True)

    # 4. drop duplicates based on the date column keeping the first occurrence 
    # which will be the valid station if it has data
    df_deduped = df.drop_duplicates('date')

    # 5. remove the station column because we are done with it
    df_deduped = df_deduped.drop(columns='station').set_index('date').sort_index()

    # 6. take valid station's WESF and fall back on station ? if it is null
    df_deduped = df_deduped.assign(
        WESF=lambda x: x.WESF.combine_first(station_qm_wesf)
    )

    df_deduped.shape
    return (df_deduped,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Here we used the `combine_first()` method to coalesce the values to the first non-null entry; this means that if we had data from both stations, we would first take the value provided by the named station and if (and only if) that station was null would we take the value from the station named `?`. The following table contains some examples of how this would play out:

    | station GHCND:USC00280907 | station ? | result of `combine_first()` |
    | :---: | :---: | :---: |
    | 1 | 17 | 1 |
    | 1 | `NaN` | 1 |
    | `NaN` | 17 | 17 |
    | `NaN` | `NaN` | `NaN` |

    Check out the 4th row&mdash;we have `WESF` in the correct spot thanks to the index:
    """
    )
    return


@app.cell
def _(df_deduped):
    df_deduped.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Dealing with nulls
    We could drop nulls, replace them with some arbitrary value, or impute them using the surrounding data. Each of these options may have ramifications, so we must choose wisely.

    We can use `dropna()` to drop rows where any column has a null value. The default options leave us hardly any data:
    """
    )
    return


@app.cell
def _(df_deduped):
    df_deduped.dropna().shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If we pass `how='all'`, we can choose to only drop rows where everything is null, but this removes nothing:""")
    return


@app.cell
def _(df_deduped):
    df_deduped.dropna(how='all').shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can use just a subset of columns to determine what to drop with the `subset` argument:""")
    return


@app.cell
def _(df_deduped):
    df_deduped.dropna(
        how='all', subset=['inclement_weather', 'SNOW', 'SNWD']
    ).shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This can also be performed along columns, and we can also require a certain number of null values before we drop the data:""")
    return


@app.cell
def _(df_deduped):
    df_deduped.dropna(axis='columns', thresh=df_deduped.shape[0] * .75).columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can choose to fill in the null values instead with `fillna()`:""")
    return


@app.cell
def _(df_deduped):
    df_deduped.loc[:,'WESF'].fillna(0, inplace=True)
    df_deduped.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    At this point we have done everything we can without distorting the data. We know that we are missing dates, but if we reindex, we don't know how to fill in the `NaN` data. With the weather data, we can't assume because it snowed one day that it will snow the next or that the temperature will be the same. For this reason, note that the next few examples are just for illustrative purposes only—just because we can do something doesn't mean we should.

    That being said, let's try to address some of remaining issues with the temperature data. We know that when `TMAX` is the temperature of the Sun, it must be because there was no measured value, so let's replace it with `NaN`. We will also do so for `TMIN` which currently uses -40°C for its placeholder when we know that the coldest temperature ever recorded in NYC was -15°F (-26.1°C) on February 9, 1934:
    """
    )
    return


@app.cell
def _(df_deduped, np):
    df_deduped_1 = df_deduped.assign(TMAX=lambda x: x.TMAX.replace(5505, np.nan), TMIN=lambda x: x.TMIN.replace(-40, np.nan))
    return (df_deduped_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We will also make an assumption that the temperature won't change drastically day-to-day. Note that this is actually a big assumption, but it will allow us to understand how `fillna()` works when we provide a strategy through the `method` parameter. The `fillna()` method gives us 2 options for the `method` parameter:
    - `'ffill'` to forward-fill
    - `'bfill'` to back-fill

    *Note that `'nearest'` is missing because we are not reindexing.*

    Here, we will use `'ffill'` to show how this works:
    """
    )
    return


@app.cell
def _(df_deduped_1):
    df_deduped_1.assign(TMAX=lambda x: x.TMAX.fillna(method='ffill'), TMIN=lambda x: x.TMIN.fillna(method='ffill')).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can use `np.nan_to_num()` to turn `np.nan` into 0 and `-np.inf`/`np.inf` into large negative or positive finite numbers:""")
    return


@app.cell
def _(df_deduped_1, np):
    df_deduped_1.assign(SNWD=lambda x: np.nan_to_num(x.SNWD)).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Depending on the data we are working with, we can use the `clip()` method as an alternative to `np.nan_to_num()`. The `clip()` method makes it possible to cap values at a specific minimum and/or maximum threshold. Since `SNWD` can't be negative, let's use `clip()` to enforce a lower bound of zero. To show how the upper bound works, let's use the value of `SNOW`:""")
    return


@app.cell
def _(df_deduped_1):
    df_deduped_1.assign(SNWD=lambda x: x.SNWD.clip(0, x.SNOW)).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can couple `fillna()` with other types of calculations. Here we replace missing values of `TMAX` with the median of all `TMAX` values, `TMIN` with the median of all `TMIN` values, and `TOBS` to the average of the `TMAX` and `TMIN` values. Since we place `TOBS` last, we have access to the imputed values for `TMIN` and `TMAX` in the calculation:""")
    return


@app.cell
def _(df_deduped_1):
    df_deduped_1.assign(TMAX=lambda x: x.TMAX.fillna(x.TMAX.median()), TMIN=lambda x: x.TMIN.fillna(x.TMIN.median()), TOBS=lambda x: x.TOBS.fillna((x.TMAX + x.TMIN) / 2)).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can also use `apply()` for running the same calculation across columns. For example, let's fill all missing values with their rolling 7-day median of their values, setting the number of periods required for the calculation to 0 to ensure we don't introduce more extra `NaN` values. Rolling calculations will be covered later on, so this is a preview:""")
    return


@app.cell
def _(df_deduped_1):
    df_deduped_1.apply(lambda x: x.fillna(x.rolling(7, min_periods=0).median())).head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The last strategy we could try is interpolation with the `interpolate()` method. We specify the `method` parameter with the interpolation strategy to use. There are many options, but we will stick with the default of `'linear'`, which will treat values as evenly spaced and place missing values in the middle of existing ones. We have some missing data, so we will reindex first. Look at January 9th, which we didn't have before—the values for `TMAX`, `TMIN`, and `TOBS` are the average of values the day prior (January 8th) and the day after (January 10th):""")
    return


@app.cell
def _(df_deduped_1, pd):
    df_deduped_1.reindex(pd.date_range('2018-01-01', '2018-12-31', freq='D')).apply(lambda x: x.interpolate()).head(10)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
