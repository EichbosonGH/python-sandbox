import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    1+1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Schnee
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.outline(label="Inhaltsverzeichnis")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Haus
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Test
    """)
    return


@app.cell
def _():
    import polars as pl
    import numpy as np

    return np, pl


@app.cell
def _(np, pl):
    n = 10000
    _x = np.random.rand(n)
    _y = np.random.randn(n)
    df = pl.DataFrame({"x":_x,"y":_y})
    df
    return (df,)


@app.cell
def test(np, x):
    import xy

    _x = np.linspace(0, 10, 1000)

    chart = xy.line_chart(
        xy.line(_x, np.sin(x), name="sin(x)"),
        xy.line(_x, np.cos(x), name="cos(x)"),
        xy.x_axis(label="x"),
        xy.y_axis(label="f(x)"),
        xy.legend(),
        title="XY Plot"
    )

    chart
    return


@app.cell
def _(df, plt):
    import xy.pyplot as xplt
    _fig, _ax = plt.subplots()
    _ax.plot(df["x"], df["y"])
    #ax.plot(x, np.cos(x), label="cos(x)")

    xplt.show()
    return


@app.cell
def _(np):
    import matplotlib.pyplot as plt

    x = np.linspace(0, 10, 1000)

    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label="sin(x)")
    ax.plot(x, np.cos(x), label="cos(x)")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("XY Plot")
    ax.legend()

    plt.show()
    return plt, x


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
