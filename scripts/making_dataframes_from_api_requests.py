# %% [markdown]
# # Making Pandas DataFrames from API Requests
# In this example, we will use the U.S. Geological Survey's API to grab a JSON object of earthquake data and convert it to a `pandas.DataFrame`.
#
# USGS API: https://earthquake.usgs.gov/fdsnws/event/1/

# %% [markdown]
# ### Get Data from API

# %%
import datetime as dt
import pandas as pd
import requests

yesterday = dt.date.today() - dt.timedelta(days=1)
api = "https://earthquake.usgs.gov/fdsnws/event/1/query"
payload = {
    "format": "geojson",
    "starttime": yesterday - dt.timedelta(days=30),
    "endtime": yesterday,
}
response = requests.get(api, params=payload)

# let's make sure the request was OK
response.status_code

# %% [markdown]
# Response of 200 means OK, so we can pull the data out of the result. Since we asked the API for a JSON payload, we can extract it from the response with the `json()` method.
#
# ### Isolate the Data from the JSON Response
# We need to check the structures of the response data to know where our data is.

# %%
earthquake_json = response.json()
earthquake_json.keys()

# %% [markdown]
# The USGS API provides information about our request in the `metadata` key. Note that your result will be different, regardless of the date range you chose, because the API includes a timestamp for when the data was pulled:

# %%
earthquake_json["metadata"]

# %% [markdown]
# Each element in the JSON array `features` is a row of data for our dataframe.

# %%
type(earthquake_json["features"])

# %% [markdown]
# Your data will be different depending on the date you run this.

# %%
earthquake_json["features"][0]

# %% [markdown]
# ### Convert to DataFrame
# We need to grab the `properties` section out of every entry in the `features` JSON array to create our dataframe.

# %%
earthquake_properties_data = [
    quake["properties"] for quake in earthquake_json["features"]
]
df = pd.DataFrame(earthquake_properties_data)
df.head()

# %% [markdown]
# ### (Optional) Write Data to CSV

# %%
df.to_csv("earthquakes.csv", index=False)
