import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Making Pandas DataFrames from API Requests
        In this example, we will use the U.S. Geological Survey's API to grab a JSON object of earthquake data and convert it to a `pandas.DataFrame`.

        USGS API: https://earthquake.usgs.gov/fdsnws/event/1/
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Get Data from API
        """
    )
    return


@app.cell
def _():
    import datetime as dt
    import pandas as pd
    import requests

    yesterday = dt.date.today() - dt.timedelta(days=1)
    api = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    payload = {
        'format': 'geojson',
        'starttime': yesterday - dt.timedelta(days=30),
        'endtime': yesterday
    }
    response = requests.get(api, params=payload)

    # let's make sure the request was OK
    response.status_code
    return pd, response


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Response of 200 means OK, so we can pull the data out of the result. Since we asked the API for a JSON payload, we can extract it from the response with the `json()` method.

        ### Isolate the Data from the JSON Response
        We need to check the structures of the response data to know where our data is.
        """
    )
    return


@app.cell
def _(response):
    earthquake_json = response.json()
    earthquake_json.keys()
    return (earthquake_json,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The USGS API provides information about our request in the `metadata` key. Note that your result will be different, regardless of the date range you chose, because the API includes a timestamp for when the data was pulled:
        """
    )
    return


@app.cell
def _(earthquake_json):
    earthquake_json['metadata']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Each element in the JSON array `features` is a row of data for our dataframe.
        """
    )
    return


@app.cell
def _(earthquake_json):
    type(earthquake_json['features'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Your data will be different depending on the date you run this.
        """
    )
    return


@app.cell
def _(earthquake_json):
    earthquake_json['features'][0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Convert to DataFrame
        We need to grab the `properties` section out of every entry in the `features` JSON array to create our dataframe.
        """
    )
    return


@app.cell
def _(earthquake_json, pd):
    earthquake_properties_data = [
        quake['properties'] for quake in earthquake_json['features']
    ]
    df = pd.DataFrame(earthquake_properties_data)
    df.head()
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### (Optional) Write Data to CSV
        """
    )
    return


@app.cell
def _(df):
    df.to_csv('earthquakes.csv', index=False)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
