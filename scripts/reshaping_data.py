# %% [markdown]
# # Reshaping Data
# 
# ## About the data
# In this notebook, we will using daily temperature data from the 
# [National Centers for Environmental Information (NCEI) API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2).
# We will use the Global Historical Climatology Network - Daily (GHCND) dataset;
# see the documentation [here](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf).
# 
# This data was collected for New York City for October 2018, using the Boonton
# 1 station (GHCND:USC00280907). It contains:
# - the daily minimum temperature (`TMIN`)
# - the daily maximum temperature (`TMAX`)
# - the daily temperature at time of observation (`TOBS`)
# 
# *Note: The NCEI is part of the National Oceanic and Atmospheric Administration (NOAA)
# and, as you can see from the URL for the API, this resource was created when
# the NCEI was called the NCDC. Should the URL for this resource change in the
# future, you can search for "NCEI weather API" to find the updated one.*
# 
# ## Setup
# We need to import `pandas` and read in the long format data to get started:

# %%
import pandas as pd

long_df = pd.read_csv(
    '../data/long_data.csv', usecols=['date', 'datatype', 'value']
).rename(
    columns={'value': 'temp_C'}
).assign(
    date=lambda x: pd.to_datetime(x.date),
    temp_F=lambda x: (x.temp_C * 9/5) + 32
)
long_df.head()

# %% [markdown]
# ## Transposing
# Transposing swaps the rows and the columns. We use the `T` attribute to do so:

# %%
long_df.set_index('date').head(6).T

# %% [markdown]
# ## Pivoting
# Going from long to wide format.
# 
# ### `pivot()`
# We can restructure our data by picking a column to go in the index (`index`), a column
# whose unique values will become column names (`columns`), and the values to place
# in those columns (`values`). The `pivot()` method can be used when we don't 
# need to perform any aggregation in addition to our restructuring (when our 
# index is unique); if this is not the case, we need the `pivot_table()` method. 

# %%
pivoted_df = long_df.pivot(
    index='date', columns='datatype', values='temp_C'
)
pivoted_df.head()

# %% [markdown]
# Now that the data is pivoted, we have wide format data that we can grab
# summary statistics with:

# %%
pivoted_df.describe()

# %% [markdown]
# We can also provide multiple values to pivot on, which will result in a hierarchical
# index:

# %%
pivoted_df = long_df.pivot(
    index='date', columns='datatype', values=['temp_C', 'temp_F']
)
pivoted_df.head()

# %% [markdown]
# With the hierarchical index, if we want to select `TMIN` in Fahrenheit, we will first
# need to select `temp_F` and then `TMIN`:

# %%
pivoted_df['temp_F']['TMIN'].head()

# %% [markdown]
# ### `unstack()`
# 
# We have been working with a single index so far; however, we can create an index from
# any number of columns with `set_index()`. This gives us an index of type `MultiIndex`, where the outermost level corresponds to the first element in the list provided to `set_index()`:

# %%
multi_index_df = long_df.set_index(['date', 'datatype'])
multi_index_df.head().index

# %% [markdown]
# Notice there are now 2 index sections of the dataframe:

# %%
multi_index_df.head()

# %% [markdown]
# With an index of type `MultiIndex`, we can no longer use `pivot()`. We must now use `unstack()`, which by default moves the innermost index onto the columns:

# %%
unstacked_df = multi_index_df.unstack()
unstacked_df.head()

# %% [markdown]
# The `unstack()` method also provides the `fill_value` parameter, which let's us fill-in any `NaN` values that might arise from this restructuring of the data. Consider the case that we have data for the average temperature on October 1, 2018, but no other date:

# %%
extra_data = long_df.append([{
    'datatype': 'TAVG', 
    'date': '2018-10-01', 
    'temp_C': 10, 
    'temp_F': 50
}]).set_index(['date', 'datatype']).sort_index()

extra_data['2018-10-01':'2018-10-02']

# %% [markdown]
# If we use `unstack()` in this case, we will have `NaN` for the `TAVG` columns every day but October 1, 2018:

# %%
extra_data.unstack().head()

# %% [markdown]
# To address this, we can pass in an appropriate `fill_value`. However, we are restricted to passing in a value for this, not a strategy (like we saw with `fillna()`), so while `-40` is definitely not be the best value, we can use it to illustrate how this works, since this is the temperature at which Fahrenheit and Celsius are equal:

# %%
extra_data.unstack(fill_value=-40).head()

# %% [markdown]
# ## Melting
# Going from wide to long format.
# 
# ### Setup

# %%
wide_df = pd.read_csv('../data/wide_data.csv')
wide_df.head()

# %% [markdown]
# ### `melt()`
# In order to go from wide format to long format, we use the `melt()` method. We have to specify:
# - `id_vars`: which column(s) uniquely identify a row in the wide format (`date`, here)
# - `value_vars`: the column(s) that contain(s) the values (`TMAX`, `TMIN`, and `TOBS`, here)
# 
# Optionally, we can also provide:
# - `value_name`: what to call the column that will contain all the values once melted
# - `var_name`: what to call the column that will contain the names of the variables being measured

# %%
melted_df = wide_df.melt(
    id_vars='date',
    value_vars=['TMAX', 'TMIN', 'TOBS'],
    value_name='temp_C',
    var_name='measurement'
)
melted_df.head()

# %% [markdown]
# ### `stack()`
# Another option is `stack()`, which will pivot the columns of the dataframe into the innermost level of the index (resulting in an index of type `MultiIndex`). To illustrate this, let's set our index to be the `date` column:

# %%
wide_df.set_index('date', inplace=True)
wide_df.head()

# %% [markdown]
# By running `stack()` now, we will create a second level in our index which will contain the column names of our dataframe (`TMAX`, `TMIN`, `TOBS`). This will leave us with a `Series` object containing the values:

# %%
stacked_series = wide_df.stack()
stacked_series.head()

# %% [markdown]
# We can use the `to_frame()` method on our `Series` object to turn it into a `DataFrame` object. Since the series doesn't have a name at the moment, we will pass in the name as an argument:

# %%
stacked_df = stacked_series.to_frame('values')
stacked_df.head()

# %% [markdown]
# Once again, we have an index of type `MultiIndex`:

# %%
stacked_df.head().index

# %% [markdown]
# Unfortunately, we don't have a name for the `datatype` level:

# %%
stacked_df.index.names

# %% [markdown]
# We can use `set_names()` to address this though:

# %%
stacked_df.index.set_names(['date', 'datatype'], inplace=True)
stacked_df.index.names


