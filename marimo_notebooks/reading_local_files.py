import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # An Introduction to Jupyter Notebooks

        Jupyter Notebooks are a file format (```*.ipynb```) that you can execute and explain your code in a step-wise format.
        > Jupyter Notebooks supports not only code execution in Python, but over 40 languages including R, Lua, Rust, and Julia with numerous [kernels](https://docs.jupyter.org/en/latest/projects/kernels.html#kernels-programming-languages).

        We can write in Markdown to write text with some level of control over your formatting.
        - [Here's a Link to Basic Markdown](https://www.markdownguide.org/basic-syntax/)
        - [Here's a link to Markdown's Extended Syntax](https://www.markdownguide.org/extended-syntax/)

        Topics We Will Cover
        - Importing different files and filetypes with [```pandas```](https://pandas.pydata.org/docs/index.html)
        - Basic Statistical Analysis of tabular data with ```pandas``` and ```numpy```
        - Creating Charts with python packages from the [Matplotlib](https://matplotlib.org/), [Plotly](https://plotly.com/python/), or [HoloViz Ecosystem](https://holoviz.org/background.html#background-why-holoviz)
        - Evaluate the potential usecases for each visualization package

        ![EvidenceOfLearning](../images/learning.gif)
        <br>
        *This is you, enjoying the learning process.*
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Step 1: Import ```pandas``` into your python program.
        """
    )
    return


@app.cell
def _():
    import pandas as pd

    # This will import the pandas and numpy packages into your Python program.

    df_json = pd.read_json('../data/food-waste-pilot/food-waste-pilot.json')
    df_csv = pd.read_csv('../data/food-waste-pilot/food-waste-pilot.csv')
    df_xlsx = pd.read_excel('../data/food-waste-pilot/food-waste-pilot.xlsx')
    return df_csv, pd


@app.cell
def _(df_csv):
    df_csv.shape
    return


@app.cell
def _(df_csv):
    df_csv.head() # Grabs the top 5 items in your Dataframe by default.
    return


@app.cell
def _(df_csv):
    df_csv.tail() # Grabs the bottom 5 items in your Dataframe by default.
    return


@app.cell
def _(df_csv):
    df_csv.columns
    return


@app.cell
def _(df_csv):
    df_csv.dtypes # Returns the data types of your columns.
    return


@app.cell
def _(df_csv):
    df_csv.describe()
    return


@app.cell
def _(df_csv):
    df_csv.info() # Returns index, column names, a count of Non-Null values, and data types.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are multiple methods to do type conversion using pandas as well.
        """
    )
    return


@app.cell
def _(df_csv, pd):
    # Oh no, we can see that our Collection Date is not the data type that we want, we need to convert it to a date value.

    df_csv['Collection Date'] = pd.to_datetime(df_csv['Collection Date'])
    return


@app.cell
def _(df_csv):
    df_csv.info()
    return


@app.cell
def _(df_csv, pd):
    # An alternative way to do this date conversion:

    df_csv['Collection Date'] = df_csv['Collection Date'].apply(pd.to_datetime)
    return


@app.cell
def _(df_csv):
    # astype() is more generic method to convert data types

    df_csv['Collection Date'] = df_csv['Collection Date'].astype('datetime64[ns]')
    return


@app.cell
def _(df_csv):
    df_csv.dtypes
    return


@app.cell
def _(df_csv):
    # Now that we have converted our Collection Date column to a datetime data type, we can use the dt.day_name() method to create a new column that contains the day of the week.

    df_csv['Day of Week'] = df_csv['Collection Date'].dt.day_name()
    return


@app.cell
def _(df_csv):
    # What if we want to know the date that we collected the most food waste?

    df_csv.loc[
        df_csv['Food Waste Collected'].idxmax(),
        ['Collection Date']
    ]
    return


@app.cell
def _(df_csv):
    # If you wanted to see our top 10 collection dates, you could do this:

    df_csv.nlargest(10,'Food Waste Collected')
    return


@app.cell
def _(df_csv):
    df_csv.nsmallest(10,'Food Waste Collected')
    return


@app.cell
def _(df_csv):
    df_csv.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## You have to make sure that `pandas` parses your dates
        """
    )
    return


@app.cell
def _(pd):
    df_csv_parsed_dates = pd.read_csv('../data/food-waste-pilot/food-waste-pilot.csv', parse_dates=True, index_col="Collection Date")
    return (df_csv_parsed_dates,)


@app.cell
def _(df_csv_parsed_dates):
    df_csv_parsed_dates.plot()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
