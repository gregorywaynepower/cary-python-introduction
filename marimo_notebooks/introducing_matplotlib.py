import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Getting Started with Matplotlib

        Pandas uses `matplotlib` to create visualizations. Therefore, before we learn how to plot with `pandas`, it's important to understand how `matplotlib` works at a high-level, which is the focus of this notebook.


        ## About the Data
        In this notebook, we will be working with 2 datasets:
        - Facebook's stock price throughout 2018 (obtained using the [`stock_analysis` package](https://github.com/stefmolin/stock-analysis))
        - Earthquake data from September 18, 2018 - October 13, 2018 (obtained from the US Geological Survey (USGS) using the [USGS API](https://earthquake.usgs.gov/fdsnws/event/1/))

        ## Setup
        We need to import `matplotlib.pyplot` for plotting.
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import pandas as pd
    return pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotting lines
        """
    )
    return


@app.cell
def _(pd, plt):
    fb = pd.read_csv(
        '../data/fb_stock_prices_2018.csv', index_col='date', parse_dates=True
    )

    plt.plot(fb.index, fb.open)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Since we are working in a Jupyter notebook, we can use the magic command `%matplotlib inline` once and not have to call `plt.show()` for each plot.
        """
    )
    return


@app.cell
def _(pd, plt):
    fb_1 = pd.read_csv('../data/fb_stock_prices_2018.csv', index_col='date', parse_dates=True)
    plt.plot(fb_1.index, fb_1.open)
    return (fb_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Scatter plots
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can pass in a string specifying the style of the plot. This is of the form `[marker][linestyle][color]`. For example, we can make a black dashed line with `'--k'` or a red scatter plot with `'or'`:
        """
    )
    return


@app.cell
def _(fb_1, plt):
    plt.plot('high', 'low', 'or', data=fb_1.head(20))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Here are some examples of how you make a format string:

        | Marker | Linestyle | Color | Format String | Result |
        | :---: | :---: | :---: | :---: | --- |
        | | `-` | `b` | `-b` | blue solid line|
        | `.` |  | `k` | `.k` | black points|
        |  | `--` | `r` | `--r` | red dashed line|
        | `o` | `-` | `g` | `o-g` | green solid line with circles|
        | | `:` | `m` | `:m` | magenta dotted line|
        |`x` | `-.` | `c` | `x-.c` | cyan dot-dashed line with x's|
 
        Note that we can also use format strings of the form `[color][marker][linestyle]`, but the parsing by `matplotlib` (in rare cases) might not be what we were aiming for. Consult the *Notes* section in the [documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) for the complete list of options.
        ## Histograms
        """
    )
    return


@app.cell
def _(pd, plt):
    quakes = pd.read_csv('../data/earthquakes.csv')
    plt.hist(quakes.query('magType == "ml"').mag)
    return (quakes,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Bin size matters
        Notice how our assumptions of the distribution of the data can change based on the number of bins (look at the drop between the two highest peaks on the righthand plot):
        """
    )
    return


@app.cell
def _(plt, quakes):
    x = quakes.query('magType == "ml"').mag
    fig, _axes = plt.subplots(1, 2, figsize=(10, 3))
    for ax, bins in zip(_axes, [7, 35]):
        ax.hist(x, bins=bins)
        ax.set_title(f'bins param: {bins}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plot components
        ### `Figure`
        Top-level object that holds the other plot components.
        """
    )
    return


@app.cell
def _(plt):
    fig_1 = plt.figure()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### `Axes`
        Individual plots contained within the `Figure`.

        ## Creating subplots
        Simply specify the number of rows and columns to create:
        """
    )
    return


@app.cell
def _(plt):
    fig_2, _axes = plt.subplots(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As an alternative to using `plt.subplots()` we can add `Axes` objects to the `Figure` object on our own. This allows for some more complex layouts, such as picture in picture:
        """
    )
    return


@app.cell
def _(plt):
    fig_3 = plt.figure(figsize=(3, 3))
    outside = fig_3.add_axes([0.1, 0.1, 0.9, 0.9])
    inside = fig_3.add_axes([0.7, 0.7, 0.25, 0.25])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating Plot Layouts with `gridspec`
        We can create subplots with varying sizes as well:
        """
    )
    return


@app.cell
def _(plt):
    fig_4 = plt.figure(figsize=(8, 8))
    gs = fig_4.add_gridspec(3, 3)
    top_left = fig_4.add_subplot(gs[0, 0])
    mid_left = fig_4.add_subplot(gs[1, 0])
    top_right = fig_4.add_subplot(gs[:2, 1:])
    bottom = fig_4.add_subplot(gs[2, :])
    return (fig_4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Saving plots
        Use `plt.savefig()` to save the last created plot. To save a specific `Figure` object, use its `savefig()` method. Which supports 'png', 'pdf', 'svg', and 'eps' filetypes.
        """
    )
    return


@app.cell
def _(fig_4):
    fig_4.savefig('empty.png')
    fig_4.savefig('empty.pdf')
    fig_4.savefig('empty.svg')
    fig_4.savefig('empty.eps')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Cleaning up
        It's important to close resources when we are done with them. We use `plt.close()` to do so. If we pass in nothing, it will close the last plot, but we can pass in the specific `Figure` object to close or say `'all'` to close all `Figure` objects that are open. Let's close all the `Figure` objects that are open with `plt.close()`:
        """
    )
    return


@app.cell
def _(plt):
    plt.close('all')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Additional plotting options
        ### Specifying figure size
        Just pass the `figsize` argument to `plt.figure()`. It's a tuple of `(width, height)`:
        """
    )
    return


@app.cell
def _(plt):
    fig_5 = plt.figure(figsize=(10, 4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This can be specified when creating subplots as well:
        """
    )
    return


@app.cell
def _(plt):
    fig_6, _axes = plt.subplots(1, 2, figsize=(10, 4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### `rcParams`
        A small subset of all the available plot settings (shuffling to get a good variation of options):
        """
    )
    return


@app.cell
def _():
    import random
    import matplotlib as mpl

    rcparams_list = list(mpl.rcParams.keys())
    random.seed(20) # make this repeatable
    random.shuffle(rcparams_list)
    sorted(rcparams_list[:20])
    return (mpl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can check the current default `figsize` using `rcParams`:
        """
    )
    return


@app.cell
def _(mpl):
    mpl.rcParams['figure.figsize']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also update this value to change the default (until the kernel is restarted):
        """
    )
    return


@app.cell
def _(mpl):
    mpl.rcParams['figure.figsize'] = (300, 10)
    mpl.rcParams['figure.figsize']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Use `rcdefaults()` to restore the defaults. Note this is slightly different than before because running `%matplotlib inline` sets a different value for `figsize` ([see more](https://github.com/ipython/ipykernel/blob/master/ipykernel/pylab/config.py#L42-L56)). After we reset, we are going back to the default value of `figsize` before that import:
        """
    )
    return


@app.cell
def _(mpl):
    mpl.rcdefaults()
    mpl.rcParams['figure.figsize']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This can also be done via `pyplot`:
        """
    )
    return


@app.cell
def _(plt):
    plt.rc('figure', figsize=(20, 20)) # change `figsize` default to (20, 20)
    plt.rcdefaults() # reset the default
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
