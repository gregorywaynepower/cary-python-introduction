import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # The `pandas.plotting` module
        Pandas provides some extra plotting functions for some new plot types.

        ## About the Data
        In this notebook, we will be working with Facebook's stock price throughout 2018 (obtained using the [`stock_analysis` package](https://github.com/stefmolin/stock-analysis)).

        ## Setup
        """
    )
    return


@app.cell
def _():
    # '%matplotlib inline' command supported automatically in marimo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    fb = pd.read_csv(
        '../data/fb_stock_prices_2018.csv', index_col='date', parse_dates=True
    )
    return fb, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Scatter matrix
        Easily create scatter plots between all columns in the dataset:
        """
    )
    return


@app.cell
def _(fb):
    from pandas.plotting import scatter_matrix
    scatter_matrix(fb, figsize=(10, 10))
    return (scatter_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Changing the diagonal from histograms to KDE:
        """
    )
    return


@app.cell
def _(fb, scatter_matrix):
    scatter_matrix(fb, figsize=(10, 10), diagonal='kde')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Lag plot
        Lag plots let us see how the variable correlates with past observations of itself. Random data has no pattern:
        """
    )
    return


@app.cell
def _(np, pd):
    from pandas.plotting import lag_plot
    np.random.seed(0) # make this repeatable
    lag_plot(pd.Series(np.random.random(size=200)))
    return (lag_plot,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Data with some level of correlation to itself (autocorrelation) may have patterns. Stock prices are highly autocorrelated:
        """
    )
    return


@app.cell
def _(fb, lag_plot):
    lag_plot(fb.close)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The default lag is 1, but we can alter this with the `lag` parameter. Let's look at a 5 day lag (a week of trading activity):
        """
    )
    return


@app.cell
def _(fb, lag_plot):
    lag_plot(fb.close, lag=5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Autocorrelation plots
        We can use the autocorrelation plot to see if this relationship may be meaningful or is just noise. Random data will not have any significant autocorrelation (it stays within the bounds below):
        """
    )
    return


@app.cell
def _(np, pd):
    from pandas.plotting import autocorrelation_plot
    np.random.seed(0) # make this repeatable
    autocorrelation_plot(pd.Series(np.random.random(size=200)))
    return (autocorrelation_plot,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Stock data, on the other hand, does have significant autocorrelation:
        """
    )
    return


@app.cell
def _(autocorrelation_plot, fb):
    autocorrelation_plot(fb.close)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Bootstrap plot
        This plot helps us understand the uncertainty in our summary statistics:
        """
    )
    return


@app.cell
def _(fb, plt):
    from pandas.plotting import bootstrap_plot
    fig = bootstrap_plot(fb.volume, fig=plt.figure(figsize=(10, 6)))
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
