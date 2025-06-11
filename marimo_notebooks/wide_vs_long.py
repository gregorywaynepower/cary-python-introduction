import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Wide vs. Long Format Data

        ## About the data
        In this notebook, we will be using daily temperature data from the [National Centers for Environmental Information (NCEI) API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2). We will use the Global Historical Climatology Network - Daily (GHCND) dataset for the Boonton 1 station (GHCND:USC00280907); see the documentation [here](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf).

        *Note: The NCEI is part of the National Oceanic and Atmospheric Administration (NOAA) and, as you can see from the URL for the API, this resource was created when the NCEI was called the NCDC. Should the URL for this resource change in the future, you can search for "NCEI weather API" to find the updated one.*

        ## Setup
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import pandas as pd

    wide_df = pd.read_csv('../data/wide_data.csv', parse_dates=['date'])
    long_df = pd.read_csv(
        '../data/long_data.csv', 
        usecols=['date', 'datatype', 'value'], 
        parse_dates=['date']
    )[['date', 'datatype', 'value']] # sort columns
    return long_df, plt, wide_df


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Wide format
        Our variables each have their own column:
        """
    )
    return


@app.cell
def _(wide_df):
    wide_df.head(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Describing all the columns is easy:
        """
    )
    return


@app.cell
def _(wide_df):
    wide_df.describe(include='all')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It's easy to graph with `pandas`:
        """
    )
    return


@app.cell
def _(plt, wide_df):
    wide_df.plot(
        x='date', y=['TMAX', 'TMIN', 'TOBS'], figsize=(15, 5), 
        title='Temperature in NYC in October 2018'
    ).set_ylabel('Temperature in Celsius')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Long format
        Our variable names are now in the `datatype` column and their values are in the `value` column. We now have 3 rows for each date, since we have 3 different `datatypes`:
        """
    )
    return


@app.cell
def _(long_df):
    long_df.head(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Since we have many rows for the same date, using `describe()` is not that helpful:
        """
    )
    return


@app.cell
def _(long_df):
    long_df.describe(include='all')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Plotting long format data in `pandas` can be rather tricky. Instead we use `seaborn`:
        """
    )
    return


@app.cell
def _(long_df, plt):
    import seaborn as sns

    sns.set(rc={'figure.figsize': (15, 5)}, style='white')

    ax = sns.lineplot(
        data=long_df, x='date', y='value', hue='datatype'
    )
    ax.set_ylabel('Temperature in Celsius')
    ax.set_title('Temperature in NYC in October 2018')
    plt.show()
    return (sns,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        With long data and `seaborn`, we can easily facet our plots:
        """
    )
    return


@app.cell
def _(long_df, plt, sns):
    sns.set(
        rc={'figure.figsize': (20, 10)}, style='white', font_scale=2
    )

    g = sns.FacetGrid(long_df, col='datatype', height=10)
    g = g.map(plt.plot, 'date', 'value')
    g.set_titles(size=25)
    g.set_xticklabels(rotation=45)
    plt.show()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
