# %% [markdown] # Wide vs. Long Format Data
# 
# ## About the data In this notebook, we will be using daily temperature data
# from the [National Centers for Environmental Information (NCEI)
# API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2). We will use the
# Global Historical Climatology Network - Daily (GHCND) dataset for the Boonton
# 1 station (GHCND:USC00280907); see the documentation
# [here](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf).
# 
# *Note: The NCEI is part of the National Oceanic and Atmospheric
# Administration (NOAA) and, as you can see from the URL for the API, this
# resource was created when the NCEI was called the NCDC. Should the URL for
# this resource change in the future, you can search for "NCEI weather API" to
# find the updated one.*
# 
# ## Setup

# %%
import matplotlib.pyplot as plt
import pandas as pd

wide_df = pd.read_csv('../data/wide_data.csv', parse_dates=['date'])
long_df = pd.read_csv( '../data/long_data.csv', usecols=['date', 'datatype', 'value'],
            parse_dates=['date'])[['date', 'datatype', 'value']] # sort columns

# %% [markdown] ## Wide format Our variables each have their own column:

# %%
wide_df.head(6)

# %% [markdown] Describing all the columns is easy:

# %%
wide_df.describe(include='all', datetime_is_numeric=True)

# %% [markdown] It's easy to graph with `pandas`:

# %%
wide_df.plot( x='date',
             y=['TMAX', 'TMIN', 'TOBS'],
             figsize=(15, 5), 
             title='Temperature in NYC in October 2018').set_ylabel('Temperature in Celsius')
plt.show()

# %% [markdown] ## Long format Our variable names are now in the
# `datatype` column and their values are in the `value` column. We
# now have 3 rows for each date, since we have 3 different
# `datatypes`:

# %%
long_df.head(6)

# %% [markdown] Since we have many rows for the same date, using
# `describe()` is not that helpful:

# %%
long_df.describe(include='all', datetime_is_numeric=True)

# %% [markdown] Plotting long format data in `pandas` can be
# rather tricky. Instead we use `seaborn`:

# %%
import seaborn as sns

sns.set(rc={'figure.figsize': (15, 5)}, style='white')

ax = sns.lineplot( data=long_df, x='date', y='value', hue='datatype')
ax.set_ylabel('Temperature in Celsius')
ax.set_title('Temperature in NYC in October 2018')

plt.show()

# %% [markdown] With long data and `seaborn`, we can easily facet
# our plots:

# %%
sns.set( rc={'figure.figsize': (20, 10)}, style='white',
        font_scale=2)

g = sns.FacetGrid(long_df, col='datatype', height=10)
g = g.map(plt.plot, 'date', 'value')

g.set_titles(size=25)
g.set_xticklabels(rotation=45)

plt.show()
