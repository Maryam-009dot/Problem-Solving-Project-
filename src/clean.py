import pandas as pd
import numpy as np

RAW = "data/raw/wdi_raw.xlsx"
OUT = "data/clean/wdi_clean.csv"

df = pd.read_excel(RAW, sheet_name="Data")
df = df[df["Country Code"].notna()].copy()

year_cols = [c for c in df.columns if "[YR" in str(c)]
df[year_cols] = df[year_cols].replace("..", np.nan).apply(pd.to_numeric)

df = df[df["Country Name"] != "Yemen, Rep."]

long = df.melt(
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    value_vars=year_cols,
    var_name="Year",
    value_name="Value",
)
long["Year"] = long["Year"].str[:4].astype(int)
long = long[long["Year"] <= 2022]

wide = long.pivot(
    index=["Country Name", "Country Code", "Year"],
    columns="Series Code",
    values="Value",
).reset_index()
wide.columns.name = None

wide.to_csv(OUT, index=False)
print(wide.shape)
print(wide["Country Name"].nunique(), "countries")
print(wide.isna().sum()) 