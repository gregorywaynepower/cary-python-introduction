# Cary Introduction to Python & Anaconda

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gregorywaynepower/cary-python-introduction/blob/main)

## Navigating the File Tree in this Repository

- For an Introduction to Data Analysis and a Refresher on Statistics
  - [introduction_to_data_analysis.ipynb](/notebooks/introduction_to_data_analysis.ipynb)
- For an Introduction to Hypothesis Testing
  - [hypothesis_testing.ipynb](/notebooks/hypothesis_testing.ipynb)
- For an Introduction to Python
  - [python_101.ipynb](/notebooks/python_101.ipynb)
- Handling Common Errors in Python
  - [python_errors.ipynb](/notebooks/python_errors.ipynb)
- Reading Local Files with `pandas` and visualizing datasets with `matplotlib`
  - [reading_local_files.ipynb](/notebooks/reading_local_files.ipynb)
- Making DataFrames from API requests
  - [making_dataframes_from_api_requests.ipynb](/notebooks/making_dataframes_from_api_requests.ipynb)
- What is wide vs long format data?
  - [wide_vs_long.ipynb](/notebooks/wide_vs_long.ipynb)
- Cleaning data in `pandas`
  - [cleaning_data.ipynb](/notebooks/cleaning_data.ipynb)
- Reshaping Data in `pandas`
  - [reshaping_data.ipynb](/notebooks/reshaping_data.ipynb)
- Handling Data Issues in `pandas`
  - [handling_data_issues.ipynb](/notebooks/handling_data_issues.ipynb)
- Introduction to [`plotly.express`](https://plotly.com/python/plotly-express/)
  - [intro_to_plotly_express.ipynb](/notebooks/intro_to_plotly_express.ipynb)
- Introduction to `matplotlib`
  - [introducing_matplotlib.ipynb](/notebooks/introducing_matplotlib.ipynb)
- Plotting with `plot()` method for `pandas` objects
  - [plotting_with_pandas.ipynb](/notebooks/plotting_with_pandas.ipynb)
- Introduction to `pandas.plotting()` module
  - [pandas_plotting_module.ipynb](/notebooks/pandas_plotting_module.ipynb)

## Installing This Repository's Depencies using `conda-lock.yml` or `environment.yml` Files

You can install project dependencies either using out-of-the-box conda CLI commands, or installing conda-lock to ensure dependencies are solved no matter the platform you are on.

```bash
conda install -c conda-forge conda-lock
conda-lock install --name name-of-your-environment conda-lock.yml
conda activate name-of-your-environment
```

```bash
conda env create -n name-of-your-environment --file environment.yml
conda activate name-of-your-environment
```

## Missing an Imported Module?

1. Install your module using `conda install name-of-module` [in your terminal or Anaconda Prompt](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#id2)
2. [Install your module with Anaconda Navigator](https://docs.anaconda.com/navigator/getting-started/#managing-packages)
   1. Open Anaconda Navigator
   2. Click Environments tab
   3. Select the Environment you want to install a module into

Please **don't use** `python -m pip install name-of-module` when installing packages without activating your conda environment via `conda activate name-of-environment` first.

[Anaconda's Explanation of conda & pip if you want a more in-depth explanation.](https://www.anaconda.com/blog/understanding-conda-and-pip "https://www.anaconda.com/blog/understanding-conda-and-pip")

## Anaconda's Free [with Account Creation] Courses

- [Getting Started with Anaconda](https://freelearning.anaconda.cloud/get-started-with-anaconda)
- [conda Basics](https://freelearning.anaconda.cloud/conda-basics)
- [Jupyter Notebook Basics](https://freelearning.anaconda.cloud/jupyter-notebook-basics)

## Anaconda Ecosystem

- [Anaconda Ecosystem Documentation](https://docs.anaconda.com/)

### Anaconda Navigator (GUI)

- [Anaconda Navigator: Getting Started](https://docs.anaconda.com/navigator/getting-started/)
- [Anaconda Navigator Documentation](https://docs.anaconda.com/navigator/)

#### Trying to Explore Packages Not Installed?

If your list of "Not Installed" packages is blank, I recommend [manually updating](https://docs.anaconda.com/navigator/update-navigator/#manual-update) Anaconda Navigator.

### conda (CLI)

- [conda: Getting Started](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [conda Documenation](https://docs.conda.io/projects/conda/en/stable/)
- [conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)

#### Need to Rollback to a Previous Version of a conda?

If you are experimenting with your `conda base` environment and need to restore a previous version of a conda.

1. You can use the `conda list` command with the `--revisions` flag to view your conda revision history.
2. You can use the `conda install` command with the `--revision` flag with the number that corresponds to the version you want to rollback to.

```bash or Powershell
conda list --revisions
conda install --revision N
# Replace N with the number that corresponds to the version you want to rollback to.
```

#### Trying to make conda Faster?

- [Anaconda: Conda is Fast Now. Like, Really Fast](https://www.anaconda.com/blog/conda-is-fast-now)
- [conda-libmamba-solver: Getting Started](https://conda.github.io/conda-libmamba-solver/getting-started/)
- [Replace it with `mamba`; even for existing `conda` installations](https://mamba.readthedocs.io/en/latest/installation.html)

## Python 3

### Official Documentation

1. [Python.org's 'Whetting Your Appetite'](https://docs.python.org/3/tutorial/appetite.html)
2. [Python.org's Official Python 3 Tutorial](https://docs.python.org/3/tutorial/ "https://docs.python.org/3/tutorial/")
3. [Python.org's Glossary of Terms](https://docs.python.org/3/glossary.html#glossary)
4. [Python.org's Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Python Modules

### `pandas`

For in-memory analysis of tabular data and introduces the DataFrame

- [Landing page for `pandas`](https://pandas.pydata.org/docs/getting_started/index.html)
- [pandas Compared to Spreadsheets](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html)
- [pandas Compared to SQL Queries](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)
- [pandas Compared to SAS](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html)

### `geopandas`

If you need your DataFrame to be mapped or do geospatial calculations.

- [Landing page for `geopandas`](https://geopandas.org/en/stable/)
- [`geopandas` User Guide](https://geopandas.org/en/stable/docs/user_guide.html)

### `folium`

If you need more interactivity from your generated map.

- [Landing page for `folium`](https://github.com/python-visualization/folium)

### `cartopy`

If you need more control over your generated static map projection.

- [Landing page for `cartopy`](https://scitools.org.uk/cartopy/docs/latest/)

### `xarray`

If you need your dataset to have more than two dimensions.

- [Landing Page for `xarray`](https://docs.xarray.dev/en/stable/)

### `polars`

If you are working with larger-than-memory datasets and want an API similar to pandas.

- [Landing Page for `polars`](https://pola-rs.github.io/polars-book/)

### `matplotlib`

Highly configurable visualization library that other libraries build off of.

- [Landing page for `matplotlib`](https://matplotlib.org/)

### `seaborn`

High-level library for generating statistical graphics, especially for long data format.

- [Landing page for `seaborn`](https://seaborn.pydata.org/)

### `plotly.express`

Generate interactive graphics, with a focus on exploratory analysis with visuals.

- [Landing page for `plotly.express`](https://plotly.com/python/plotly-express/)

## Recommended Books

I highly recommend going through the official Python 3 tutorial first. It's a great way to get your feet wet and get a feel for the language. However, here are some books I recommend if you want to go deeper or explore certain topics.

1. [Automate the Boring Stuff with Python by Al Sweigart](https://automatetheboringstuff.com/)
2. [Data Analysis with Pandas: 2nd Edition by Stefanie Molin](https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas-2nd-edition)
3. [Data Science at the Command Line: 2nd Edition by Jeoroen Janssens](https://jeroenjanssens.com/dsatcl/)

## Youtube Resources to Check Out

1. [Rob Mulla on YouTube for Data Science with Focus on Python](https://www.youtube.com/@robmulla "https://www.youtube.com/@robmulla")
   1. [Playlist: Medallion Python Data Science Coding Videos](https://www.youtube.com/playlist?list=PL7RwtdVQXQ8qxBH6ugYn50D0M5u--2Xx4 "https://www.youtube.com/playlist?list=pl7rwtdvqxq8qxbh6ugyn50d0m5u--2xx4")
   2. [Playlist: Working with Data in Python](https://www.youtube.com/playlist?list=PL7RwtdVQXQ8oYpuIIDWR0SaaSCe8ZeZ7t "https://www.youtube.com/playlist?list=pl7rwtdvqxq8oypuiidwr0saasce8zez7t")
2. [Conference Talk: So you want to be a Python expert?](https://www.youtube.com/watch?v=cKPlPJyQrt4)
3. [Conference Talk: 1000x faster data manipulation: vectorizing with `pandas` and `numpy`](https://www.youtube.com/watch?v=nxWginnBklU "https://www.youtube.com/watch?v=nxWginnBklU")
4. [Conference Talk: No More Sad Pandas: Optimizing Pandas Code for Sped and Efficiency](https://www.youtube.com/watch?v=HN5d490_KKk)
5. [Conference Talk: Effective Pandas](https://www.youtube.com/watch?v=zgbUk90aQ6A)
6. [Conference Tutorial: So You Wanna Be a Pandas Expert?](https://www.youtube.com/watch?v=pjq3QOxl9Ok)

## Topics on the Table

- Installing [Anaconda's](https://www.anaconda.com/) Package & Environment Manager [`conda`](https://docs.conda.io/projects/conda/en/stable/) (Command Line Interface Tool) and [Anaconda-Navigator](https://docs.anaconda.com/navigator/index.html) (Graphical User Interface Tool) (Best practice when it comes to dependency management for Python and R)
- Picking an editor of your choice that supports JupyterNotebooks ([Visual Studio Code](https://code.visualstudio.com/) or [JupyterLab](https://jupyter.org/))
- How do I get data into Python and get descriptive statistics? (reading files with [pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started))
- Now paint me a picture with the data. (introduction to [Plotly](https://plotly.com/python/) & [Holoviz Ecosystem](https://holoviz.org/index.html))
- How do I share this?
  - [Binder](https://mybinder.org/) if you want interactivity (a little more setup)
  - [nbviewer](https://nbviewer.org/) if you value sharing your rendered files (less setup but not as pretty)

## Sidequests

- How to work with the Terminal
  - [Using Powershell](https://learn.microsoft.com/en-us/powershell/scripting/overview)
- Basics of version control using Git & pushing to Github
  - [Official Git Documentation & Cheatsheets](https://git-scm.com/doc)
  - [Git & Github Crash Course for Beginners](https://www.youtube.com/watch?v=HVsySz-h9r4&list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx&index=1)
  - [Want Richer Change History for Notebooks? Try ReviewNB](https://www.reviewnb.com)

If you have anything you want to cover, I'm open to suggestions. My previous experience with python covers web scraping, cleaning data, statistical analysis, and moving data into and out of databases.
