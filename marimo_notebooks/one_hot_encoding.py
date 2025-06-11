import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # One-Hot Encoding

        ## Why Bother with One-Hot Encoding?

        It's useful for feeding categorical data into machine-learning algorithms since integers are computationally less expensive than strings.
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    print(pd.__version__)
    return (pd,)


@app.cell
def _(pd):
    disengagements = pd.read_excel("../data/cassi-autonomous-shuttle/autonomous_shuttle_disengagement.xlsx",usecols=["Incident Datetime", "Location","Weather","Vehicle Speed in Miles per Hour", "Initiated by","Cause"], parse_dates=True)
    disengagements
    return (disengagements,)


@app.cell
def _(disengagements):
    disengagements.dtypes
    return


@app.cell
def _(disengagements, pd):
    disengagements['Incident Datetime'] = pd.to_datetime(disengagements['Incident Datetime'], utc=True)
    disengagements['Initiated by'] = disengagements['Initiated by'].astype('category')
    disengagements['Cause'] = disengagements['Cause'].astype('category')
    disengagements.dtypes
    return


@app.cell
def _(disengagements):
    disengagements_1 = disengagements.assign(week_of_year=disengagements['Incident Datetime'].dt.isocalendar().week, week_of_pilot=lambda x: disengagements['Incident Datetime'].dt.isocalendar().week - 9)
    disengagements_1
    return (disengagements_1,)


@app.cell
def _(disengagements_1):
    disengagements_1['Cause']
    return


@app.cell
def _(disengagements_1):
    disengagements_1['Cause'].cat.categories
    return


@app.cell
def _(disengagements_1):
    disengagements_datetime_is_index = disengagements_1.set_index('Incident Datetime')
    disengagements_datetime_is_index
    return (disengagements_datetime_is_index,)


@app.cell
def _(disengagements_datetime_is_index):
    disengagements_datetime_is_index.index=disengagements_datetime_is_index.index.tz_convert(tz='US/Eastern')
    disengagements_datetime_is_index
    return


@app.cell
def _(disengagements_datetime_is_index):
    disengagements_datetime_is_index.dtypes
    return


@app.cell
def _(disengagements_datetime_is_index):
    one_hot = disengagements_datetime_is_index.Weather.str.get_dummies(sep=';')
    one_hot
    return (one_hot,)


@app.cell
def _(one_hot):
    one_hot.columns = 'Weather_' + one_hot.columns
    one_hot
    return


@app.cell
def _(disengagements_datetime_is_index):
    one_hot_cause = disengagements_datetime_is_index.Cause.str.get_dummies()
    one_hot_cause.columns = 'Cause_' + one_hot_cause.columns
    one_hot_cause
    return (one_hot_cause,)


@app.cell
def _(disengagements_datetime_is_index, one_hot, one_hot_cause, pd):
    disengagements_datetime_is_index_1 = disengagements_datetime_is_index.drop(['Weather', 'Initiated by', 'Cause'], axis=1)
    cassi_data_one_hot_encoded = pd.concat([disengagements_datetime_is_index_1, one_hot, one_hot_cause], axis=1)
    cassi_data_one_hot_encoded
    return (cassi_data_one_hot_encoded,)


@app.cell
def _(cassi_data_one_hot_encoded):
    cassi_data_one_hot_encoded.index = cassi_data_one_hot_encoded.index.tz_convert(tz='UTC')
    return


@app.cell
def _(cassi_data_one_hot_encoded):
    cassi_data_one_hot_encoded
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
