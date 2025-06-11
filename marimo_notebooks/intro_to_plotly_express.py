import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import plotly.express as px

    df = px.data.gapminder().query("year==2007")
    return df, px


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df, px):
    px.strip(df, x='lifeExp', hover_name="country")
    return


@app.cell
def _(df, px):
    px.strip(df, x='lifeExp', color="continent", hover_name="country")
    return


@app.cell
def _(df, px):
    px.histogram(df, x='lifeExp', color="continent", hover_name="country")
    return


@app.cell
def _(df, px):
    px.histogram(df, x='lifeExp', color="continent", hover_name="country", marginal="rug")
    return


@app.cell
def _(df, px):
    px.histogram(df, x='lifeExp', y="pop", color="continent", hover_name="country", marginal="rug")
    return


@app.cell
def _(df, px):
    px.histogram(df, x='lifeExp', y="pop", color="continent", hover_name="country", marginal="rug", facet_col="continent")
    return


@app.cell
def _(df, px):
    px.bar(df, color='lifeExp', x="pop", y="continent", hover_name="country")
    return


@app.cell
def _(df, px):
    px.sunburst(df, color='lifeExp', values="pop", path=["continent", "country"], hover_name="country", height=500)
    return


@app.cell
def _(df, px):
    px.treemap(df, color='lifeExp', values="pop", path=["continent", "country"], hover_name="country", height=500)
    return


@app.cell
def _(df, px):
    px.choropleth(df, color='lifeExp', locations="iso_alpha", hover_name="country", height=500)
    return


@app.cell
def _(df, px):
    px.scatter(df, x="gdpPercap", y='lifeExp', hover_name="country", height=500)
    return


@app.cell
def _(df, px):
    px.scatter(df, x="gdpPercap", y='lifeExp', hover_name="country", color="continent",size="pop", height=500)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can see that the curve follows a logarithmic path, so make `log_x=True` to straighten out the line to view the relationships in an easier manner. In the graph below we can view the [monotic and nonmonotonic relationships](https://www.statology.org/monotonic-relationship/) in the dataset.

        """
    )
    return


@app.cell
def _(df, px):
    px.scatter(df, x="gdpPercap", y='lifeExp', hover_name="country", color="continent",size="pop", size_max=60, log_x=True, height=500)
    return


@app.cell
def _(df, px):
    fig = px.scatter(df, x="gdpPercap", y='lifeExp', hover_name="country", color="continent",size="pop", size_max=60, log_x=True, height=500)
    return (fig,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This will allow you to inspect the values for each of these cells, unfortunately this is a great deal easier to see in JupyterLab.

        """
    )
    return


@app.cell
def _(fig):
    fig.show("json")
    return


@app.cell
def _(px):
    df_1 = px.data.gapminder().query('year == 2007')
    fig_1 = px.scatter(df_1, x='gdpPercap', y='lifeExp', color='continent', log_x=True, size='pop', size_max=60, hover_name='country', height=600, width=1000, template='simple_white', color_discrete_sequence=px.colors.qualitative.G10, title='Health vs Wealth 2007', labels=dict(continent='Continent', pop='Population', gdpPercap='GDP per Capita (US$, price-adjusted)', lifeExp='Life Expectancy (years)'))
    fig_1.update_layout(font_family='Rockwell', legend=dict(orientation='h', title='', y=1.1, x=1, xanchor='right', yanchor='bottom'))
    fig_1.update_xaxes(tickprefix='$', range=[2, 5], dtick=1)
    fig_1.update_yaxes(range=[30, 90])
    fig_1.add_hline((df_1['lifeExp'] * df_1['pop']).sum() / df_1['pop'].sum(), line_width=1, line_dash='dot')
    fig_1.add_vline((df_1['gdpPercap'] * df_1['pop']).sum() / df_1['pop'].sum(), line_width=1, line_dash='dot')
    fig_1.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Animations in Plotly Express


        """
    )
    return


@app.cell
def _(px):
    df_animation = px.data.gapminder()

    anim_fig = px.scatter(df_animation, x="gdpPercap", y="lifeExp",
                          title="Health vs Wealth from 1952 to 2007",
                          labels=dict(continent="Continent", pop="Population", gdpPercap="GDP per Capita (US$, price-adjusted)", lifeExp="Life Expectancy (years)"),
                          animation_frame="year", animation_group="country",
                          size="pop",
                          color="continent",
                          hover_name="country",
                          height=600,width=1000,
                          template="simple_white",
                          color_discrete_sequence=px.colors.qualitative.G10,
                          log_x=True,
                          size_max=60,
                          range_x=[100,100000],
                          range_y=[25,90])

    anim_fig.update_layout(font_family="Rockwell",
                      legend=dict(orientation="h", title="", y=1.1, x=1, xanchor="right", yanchor="bottom"))
    anim_fig.update_xaxes(tickprefix="$", range=[2,5], dtick=1)
    return (anim_fig,)


@app.cell
def _(anim_fig):
    anim_fig.write_html("gapminder_animation.html", auto_play=False) # You're able to export this animation.
    return


@app.cell
def _(px):
    px.defaults.height=600
    return


@app.cell
def _(px):
    z = [[0.1, 0.3, 0.5, 0.7, 0.9], [1, 0.8, 0.6, 0.4, 0.2], [0.2, 0, 0.5, 0.7, 0.9], [0.9, 0.8, 0.4, 0.2, 0], [0.3, 0.4, 0.5, 0.7, 1]]
    fig_2 = px.imshow(z, text_auto=True)
    fig_2.show()
    return


@app.cell
def _(px):
    df_2 = px.data.wind()
    fig_3 = px.bar_polar(df_2, r='frequency', theta='direction', height=600, color='strength', template='plotly_dark', color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig_3.show()
    return


@app.cell
def _(px):
    df_3 = px.data.iris()
    fig_4 = px.parallel_coordinates(df_3, color='species_id', labels={'species_id': 'Species', 'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length', 'petal_width': 'Petal Width', 'petal_length': 'Petal Length'}, color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
    fig_4.show()
    return


@app.cell
def _(px):
    df_4 = px.data.tips()
    fig_5 = px.parallel_categories(df_4, color='size', color_continuous_scale=px.colors.sequential.Inferno)
    fig_5.show()
    return


@app.cell
def _(px):
    df_5 = px.data.iris()
    fig_6 = px.parallel_coordinates(df_5, color='species_id', labels={'species_id': 'Species', 'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length', 'petal_width': 'Petal Width', 'petal_length': 'Petal Length'}, color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
    fig_6.show()
    return


@app.cell
def _(px):
    df_6 = px.data.tips()
    fig_7 = px.parallel_categories(df_6, color='size', color_continuous_scale=px.colors.sequential.Inferno)
    fig_7.show()
    return


@app.cell
def _(px):
    df_7 = px.data.election()
    fig_8 = px.scatter_ternary(df_7, a='Joly', b='Coderre', c='Bergeron', color='winner', size='total', hover_name='district', size_max=15, color_discrete_map={'Joly': 'blue', 'Bergeron': 'green', 'Coderre': 'red'})
    fig_8.show()
    return


@app.cell
def _(px):
    df_8 = px.data.election()
    fig_9 = px.scatter_3d(df_8, x='Joly', y='Coderre', z='Bergeron', color='winner', size='total', hover_name='district', symbol='result', color_discrete_map={'Joly': 'blue', 'Bergeron': 'green', 'Coderre': 'red'})
    fig_9.show()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
