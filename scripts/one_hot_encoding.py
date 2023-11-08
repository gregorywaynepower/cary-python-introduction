# %%
import pandas as pd

print(pd.__version__)

# %%
disengagements = pd.read_excel(
    "../data/cassi-autonomous-shuttle/autonomous_shuttle_disengagement.xlsx",
    usecols=[
        "Incident Datetime",
        "Location",
        "Weather",
        "Vehicle Speed in Miles per Hour",
        "Initiated by",
        "Cause",
    ],
    parse_dates=True,
)
disengagements

# %%
disengagements.dtypes

# %%
disengagements["Incident Datetime"] = pd.to_datetime(
    disengagements["Incident Datetime"], utc=True
)
disengagements["Initiated by"] = disengagements["Initiated by"].astype("category")
disengagements["Cause"] = disengagements["Cause"].astype("category")
disengagements.dtypes

# %%
disengagements = disengagements.assign(
    week_of_year=disengagements["Incident Datetime"].dt.isocalendar().week,
    week_of_pilot=lambda x: disengagements["Incident Datetime"].dt.isocalendar().week
    - 9,
)
disengagements

# %%
disengagements["Cause"]

# %%
disengagements["Cause"].cat.categories

# %%
disengagements_datetime_is_index = disengagements.set_index("Incident Datetime")
disengagements_datetime_is_index

# %%
disengagements_datetime_is_index.index = (
    disengagements_datetime_is_index.index.tz_convert(tz="US/Eastern")
)
disengagements_datetime_is_index

# %%
disengagements_datetime_is_index.dtypes

# %%
one_hot = disengagements_datetime_is_index.Weather.str.get_dummies(sep=";")
one_hot

# %%
one_hot.columns = "Weather_" + one_hot.columns
one_hot

# %%
disengagements_datetime_is_index = disengagements_datetime_is_index.drop(
    ["Weather", "Initiated by"], axis=1
)
cassi_data = pd.concat([disengagements_datetime_is_index, one_hot], axis=1)
cassi_data

# %%
cassi_data.index = cassi_data.index.tz_convert(tz="UTC")

# %%
cassi_data
