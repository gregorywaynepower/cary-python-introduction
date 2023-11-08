# %%
import plotly.express as px

df = px.data.gapminder().query("year==2007")

# %%
df.columns

# %%
df.describe()

# %%
px.strip(df, x="lifeExp", hover_name="country")

# %%
px.strip(df, x="lifeExp", color="continent", hover_name="country")

# %%
px.histogram(df, x="lifeExp", color="continent", hover_name="country")


# %%
px.histogram(df, x="lifeExp", color="continent", hover_name="country", marginal="rug")

# %%
px.histogram(
    df, x="lifeExp", y="pop", color="continent", hover_name="country", marginal="rug"
)

# %%
px.histogram(
    df,
    x="lifeExp",
    y="pop",
    color="continent",
    hover_name="country",
    marginal="rug",
    facet_col="continent",
)

# %%
px.bar(df, color="lifeExp", x="pop", y="continent", hover_name="country")

# %%
px.sunburst(
    df,
    color="lifeExp",
    values="pop",
    path=["continent", "country"],
    hover_name="country",
    height=500,
)


# %%
px.treemap(
    df,
    color="lifeExp",
    values="pop",
    path=["continent", "country"],
    hover_name="country",
    height=500,
)

# %%
px.choropleth(
    df, color="lifeExp", locations="iso_alpha", hover_name="country", height=500
)


# %%
px.scatter(df, x="gdpPercap", y="lifeExp", hover_name="country", height=500)

# %%
px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    hover_name="country",
    color="continent",
    size="pop",
    height=500,
)

# %% [markdown]
# We can see that the curve follows a logarithmic path, so make `log_x=True` to
# straighten out the line to view the relationships in an easier manner. In the
# graph below we can view the [monotic and nonmonotonic
# relationships](https://www.statology.org/monotonic-relationship/) in the
# dataset.
#

# %%
px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    hover_name="country",
    color="continent",
    size="pop",
    size_max=60,
    log_x=True,
    height=500,
)

# %%
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    hover_name="country",
    color="continent",
    size="pop",
    size_max=60,
    log_x=True,
    height=500,
)

# %% [markdown]
# This will allow you to inspect the values for each of these cells,
# unfortunately this is a great deal easier to see in JupyterLab.
#

# %%
fig.show("json")

# %%
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    log_x=True,
    size="pop",
    size_max=60,
    hover_name="country",
    height=600,
    width=1000,
    template="simple_white",
    color_discrete_sequence=px.colors.qualitative.G10,
    title="Health vs Wealth 2007",
    labels=dict(
        continent="Continent",
        pop="Population",
        gdpPercap="GDP per Capita (US$, price-adjusted)",
        lifeExp="Life Expectancy (years)",
    ),
)

fig.update_layout(
    font_family="Rockwell",
    legend=dict(
        orientation="h", title="", y=1.1, x=1, xanchor="right", yanchor="bottom"
    ),
)
fig.update_xaxes(tickprefix="$", range=[2, 5], dtick=1)
fig.update_yaxes(range=[30, 90])
fig.add_hline(
    (df["lifeExp"] * df["pop"]).sum() / df["pop"].sum(), line_width=1, line_dash="dot"
)
fig.add_vline(
    (df["gdpPercap"] * df["pop"]).sum() / df["pop"].sum(), line_width=1, line_dash="dot"
)
fig.show()

# fig.write_image("gapminder_2007.svg") # static export
# fig.write_html("gapminder_2007.html") # interactive export
# fig.write_json("gapminder_2007.json") # serialized export

# %% [markdown]
# ## Animations in Plotly Express
#
#

# %%
df_animation = px.data.gapminder()

anim_fig = px.scatter(
    df_animation,
    x="gdpPercap",
    y="lifeExp",
    title="Health vs Wealth from 1952 to 2007",
    labels=dict(
        continent="Continent",
        pop="Population",
        gdpPercap="GDP per Capita (US$, price-adjusted)",
        lifeExp="Life Expectancy (years)",
    ),
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    height=600,
    width=1000,
    template="simple_white",
    color_discrete_sequence=px.colors.qualitative.G10,
    log_x=True,
    size_max=60,
    range_x=[100, 100000],
    range_y=[25, 90],
)

anim_fig.update_layout(
    font_family="Rockwell",
    legend=dict(
        orientation="h", title="", y=1.1, x=1, xanchor="right", yanchor="bottom"
    ),
)
anim_fig.update_xaxes(tickprefix="$", range=[2, 5], dtick=1)

# %%
anim_fig.write_html(
    "gapminder_animation.html", auto_play=False
)  # You're able to export this animation.

# %%
px.defaults.height = 600

# %%
import plotly.express as px

z = [
    [0.1, 0.3, 0.5, 0.7, 0.9],
    [1, 0.8, 0.6, 0.4, 0.2],
    [0.2, 0, 0.5, 0.7, 0.9],
    [0.9, 0.8, 0.4, 0.2, 0],
    [0.3, 0.4, 0.5, 0.7, 1],
]

fig = px.imshow(z, text_auto=True)
fig.show()

# %%
import plotly.express as px

df = px.data.wind()
fig = px.bar_polar(
    df,
    r="frequency",
    theta="direction",
    height=600,
    color="strength",
    template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Plasma_r,
)
fig.show()

# %%
df = px.data.iris()
fig = px.parallel_coordinates(
    df,
    color="species_id",
    labels={
        "species_id": "Species",
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_width": "Petal Width",
        "petal_length": "Petal Length",
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2,
)
fig.show()

# %%
df = px.data.tips()
fig = px.parallel_categories(
    df, color="size", color_continuous_scale=px.colors.sequential.Inferno
)
fig.show()

# %%
df = px.data.iris()
fig = px.parallel_coordinates(
    df,
    color="species_id",
    labels={
        "species_id": "Species",
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_width": "Petal Width",
        "petal_length": "Petal Length",
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2,
)
fig.show()

# %%
df = px.data.tips()
fig = px.parallel_categories(
    df, color="size", color_continuous_scale=px.colors.sequential.Inferno
)
fig.show()

# %%
df = px.data.election()
fig = px.scatter_ternary(
    df,
    a="Joly",
    b="Coderre",
    c="Bergeron",
    color="winner",
    size="total",
    hover_name="district",
    size_max=15,
    color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"},
)
fig.show()

# %%
df = px.data.election()
fig = px.scatter_3d(
    df,
    x="Joly",
    y="Coderre",
    z="Bergeron",
    color="winner",
    size="total",
    hover_name="district",
    symbol="result",
    color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"},
)
fig.show()
