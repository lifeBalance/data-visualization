# Data Visualization
Getting familiar with [Matplotlib](https://matplotlib.org/) and [Plotly](https://plotly.com/python/).

## Poetry
To manage project dependencies and virtual environment I used [Poetry](https://python-poetry.org/). I don't like so much use the `new` subcommand, because it generates some extra scaffolding I rarely intend to use. Instead, I much prefer the `init` subcommand, which only generates the `pyproject.toml` file.

```
cd project_folder
poetry init
```

> Instructions above assume Poetry is already installed in your system.

That will start an interactive dialog to collect details about the project. Once that's done, to create and activate the virtual environment we run:

```
poetry shell
```

To install dependencies in our virtual environment:

```
poetry add matplotlib
```

That also adds them to the `pyproject.toml` file.
