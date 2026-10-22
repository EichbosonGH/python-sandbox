import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    1+1
    return


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _(toc):
    [toc]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Test
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np, pl):
    n = 1000
    x = np.random.rand(n)
    y = np.random.rand(n)
    df = pl.DataFrame({"x":x,"y":y})
    df
    return


@app.cell
def _():
    import numpy as np
    import xy.pyplot as plt

    x = np.linspace(0, 10, 1000)

    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label="sin(x)")
    ax.plot(x, np.cos(x), label="cos(x)")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("XY Plot")
    ax.legend()

    plt.show()
    return (np,)


if __name__ == "__main__":
    app.run()
