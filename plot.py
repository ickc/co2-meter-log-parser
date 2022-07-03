# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: all310-conda-forge
#     language: python
#     name: all310-conda-forge
# ---

# %%
from pathlib import Path

import pandas as pd

from co2_meter.data import Data

pd.options.plotting.backend = "plotly"

# %%
path = Path("log")

# %%
data = Data.from_dir(path)

# %%
data.dataframe

# %%
data.dataframe.describe()

# %%
data.plot()
