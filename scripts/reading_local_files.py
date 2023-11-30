# %% [markdown]
# # An Introduction to Jupyter Notebooks
#
# Jupyter Notebooks are a file format (```*.ipynb```) that you can execute and explain your code in a step-wise format.
# > Jupyter Notebooks supports not only code execution in Python, but over 40 languages including R, Lua, Rust, and Julia with numerous [kernels](https://docs.jupyter.org/en/latest/projects/kernels.html#kernels-programming-languages).
#
# We can write in Markdown to write text with some level of control over your formatting.
# - [Here's a Link to Basic Markdown](https://www.markdownguide.org/basic-syntax/)
# - [Here's a link to Markdown's Extended Syntax](https://www.markdownguide.org/extended-syntax/)
#
# Topics We Will Cover
# - Importing different files and filetypes with [```pandas```](https://pandas.pydata.org/docs/index.html)
# - Basic Statistical Analysis of tabular data with ```pandas``` and ```numpy```
# - Creating Charts with python packages from the [Matplotlib](https://matplotlib.org/), [Plotly](https://plotly.com/python/), or [HoloViz Ecosystem](https://holoviz.org/background.html#background-why-holoviz)
# - Evaluate the potential usecases for each visualization package
#
# ![EvidenceOfLearning](../images/learning.gif)
# <br>
# *This is you, enjoying the learning process.*

# %% [markdown]
# Step 1: Import ```pandas``` into your python program.

# %%
import pandas as pd

# This will import the pandas and numpy packages into your Python program.

df_json = pd.read_json("../data/food-waste-pilot/food-waste-pilot.json")
df_csv = pd.read_csv("../data/food-waste-pilot/food-waste-pilot.csv")
df_xlsx = pd.read_excel("../data/food-waste-pilot/food-waste-pilot.xlsx")

# %%
df_csv.shape

# %%
df_csv.head()  # Grabs the top 5 items in your Dataframe by default.

# %%
df_csv.tail()  # Grabs the bottom 5 items in your Dataframe by default.

# %%
df_csv.columns

# %%
df_csv.dtypes  # Returns the data types of your columns.

# %%
df_csv.describe()

# %%
df_csv.info()  # Returns index, column names, a count of Non-Null values, and data types.

# %% [markdown]
# There are multiple methods to do type conversion using pandas as well.

# %%
# Oh no, we can see that our Collection Date is not the data type that we want, we need to convert it to a date value.

df_csv["Collection Date"] = pd.to_datetime(df_csv["Collection Date"])

# %%
df_csv.info()

# %%
# An alternative way to do this date conversion:

df_csv["Collection Date"] = df_csv["Collection Date"].apply(pd.to_datetime)

# %%
# astype() is more generic method to convert data types

df_csv["Collection Date"] = df_csv["Collection Date"].astype("datetime64[ns]")

# %%
df_csv.dtypes

# %%
# Now that we have converted our Collection Date column to a datetime data type, we can use the dt.day_name() method to create a new column that contains the day of the week.

df_csv["Day of Week"] = df_csv["Collection Date"].dt.day_name()

# %%
# What if we want to know the date that we collected the most food waste?

df_csv.loc[df_csv["Food Waste Collected"].idxmax(), ["Collection Date"]]

# %%
# If you wanted to see our top 10 collection dates, you could do this:

df_csv.nlargest(10, "Food Waste Collected")

# %%
df_csv.nsmallest(10, "Food Waste Collected")

# %%
df_csv.plot()

# %% [markdown]
# ## You have to make sure that `pandas` parses your dates

# %%
df_csv_parsed_dates = pd.read_csv(
    "../data/food-waste-pilot/food-waste-pilot.csv",
    parse_dates=True,
    index_col="Collection Date",
)

# %%
df_csv_parsed_dates.plot()
