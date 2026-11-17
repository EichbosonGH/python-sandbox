import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Imports
    """)
    return


@app.cell
def _():
    from datetime import date
    from pathlib import Path

    import numpy as np
    import polars as pl

    return


if __name__ == "__main__":
    app.run()
