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

## Matplotlib shortcuts
Press `q` to close the window.

## Issues

### No GUI backend
If when you try to run the script (python mpl_squares.py) you get the error:
```
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend,
so cannot show the figure.
```

You need to install a GUI backend; in Fedora you'd do:
```
sudo dnf install python3-tkinter
```

### Seaborn error
If you try to set the style of the plot using `plt.style.use('seaborn')`, you may get the **warning**:

```
MatplotlibDeprecationWarning: The seaborn styles shipped by Matplotlib are deprecated since 3.6, as they no longer correspond to the styles shipped by seaborn. However, they will remain available as 'seaborn-v0_8-<style>'. Alternatively, directly use the seaborn API instead.
```

If it bothers you, there are two options to get rid of it:

1. Add the `-v0_8-` prefix, before the seaborn style you want to use, e.g. `seaborn-v0_8-colorblind`.
2. Install the [seaborn library](https://seaborn.pydata.org/), import it into your project, and configure it to your liking:

 - To install it.
 ```
 poetry add seaborn
 ```

 - To import it and use it:
 ```python
 import seaborn as sns

 sns.set_style('ticks')         # setting style
 sns.set_context('paper')       # setting context
 sns.set_palette('colorblind')  # setting palette
 ```

### Either show the plot in viewer or print to a file
But don't try both, otherwise the generated png is a blank file.

 > Note, none of the approaches above worked for me :-(