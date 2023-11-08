# %% [markdown]
# # The `pandas.plotting` module
# Pandas provides some extra plotting functions for some new plot types.
#
# ## About the Data
# In this notebook, we will be working with Facebook's stock price throughout 2018 (obtained using the [`stock_analysis` package](https://github.com/stefmolin/stock-analysis)).
#
# ## Setup

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fb = pd.read_csv("../data/fb_stock_prices_2018.csv", index_col="date", parse_dates=True)

# %% [markdown]
# ## Scatter matrix
# Easily create scatter plots between all columns in the dataset:

# %%
from pandas.plotting import scatter_matrix

scatter_matrix(fb, figsize=(10, 10))

# %% [markdown]
# Changing the diagonal from histograms to KDE:

# %%
scatter_matrix(fb, figsize=(10, 10), diagonal="kde")

# %% [markdown]
# ## Lag plot
# Lag plots let us see how the variable correlates with past observations of itself. Random data has no pattern:

# %%
from pandas.plotting import lag_plot

np.random.seed(0)  # make this repeatable
lag_plot(pd.Series(np.random.random(size=200)))

# %% [markdown]
# Data with some level of correlation to itself (autocorrelation) may have patterns. Stock prices are highly autocorrelated:

# %%
lag_plot(fb.close)

# %% [markdown]
# The default lag is 1, but we can alter this with the `lag` parameter. Let's look at a 5 day lag (a week of trading activity):

# %%
lag_plot(fb.close, lag=5)

# %% [markdown]
# ## Autocorrelation plots
# We can use the autocorrelation plot to see if this relationship may be meaningful or is just noise. Random data will not have any significant autocorrelation (it stays within the bounds below):

# %%
from pandas.plotting import autocorrelation_plot

np.random.seed(0)  # make this repeatable
autocorrelation_plot(pd.Series(np.random.random(size=200)))

# %% [markdown]
# Stock data, on the other hand, does have significant autocorrelation:

# %%
autocorrelation_plot(fb.close)

# %% [markdown]
# ## Bootstrap plot
# This plot helps us understand the uncertainty in our summary statistics:

# %%
from pandas.plotting import bootstrap_plot

fig = bootstrap_plot(fb.volume, fig=plt.figure(figsize=(10, 6)))
