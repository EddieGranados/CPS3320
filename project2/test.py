import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## DataFrame object, different ways to create the same

df = pd.DataFrame([[909976, 8615246, 2872086, 2273305],
                   ["Sweden", "United kingdom", "Italy", "France"]])

print(df,"\n")

df = pd.DataFrame([[909976, "Sweden"],
                   [8615246, "United kingdom"],
                   [2872086, "Italy"],
                   [2273305, "France"]])

print(df, "\n")

df.index = ["Stockholm", "London", "Rome", "Paris"]

df.columns = ["Population", "State"]

print(df, "\n")

df = pd.DataFrame([[909976, "Sweden"],
                   [8615246, "United kingdom"],
                   [2872086, "Italy"],
                   [2273305, "France"]],
                  index=["Stockholm", "London", "Rome", "Paris"],
                  columns=["Population", "State"])

print(df, "\n")

df = pd.DataFrame({"Population": [909976, 8615246, 2872086, 2273305],
                   "State": ["Sweden", "United kingdom", "Italy", "France"]},
                  index=["Stockholm", "London", "Rome", "Paris"])

print(df, "\n")

print(df.index, "\n")

print(df.columns, "\n")

print(df.values, "\n")

print(df.Population, "\n")

print(df["Population"], "\n")

print(type(df.Population),"\n")

print(df.Population.Stockholm, "\n")

print(type(df.index), "\n")

print(df.loc["Stockholm"],"\n")

print(type(df.loc["Stockholm"]),"\n")

print(df.loc[["Paris", "Rome"]],"\n")

print(print(df.loc[["Paris", "Rome"], "Population"]), "\n")

print(df.loc["Paris", "Population"],"\n")

print(df.mean(),"\n")

print(df.info(),"\n")

df.dtypes

df.head()

"""## Larger dataset"""

df_pop = pd.read_csv("european_cities.csv", delimiter=",",
                     encoding='unicode_escape', header=0)

# df_pop.head()

# df_pop.info()

# df_pop.head()

df_pop["NumericPopulation"] = df_pop.Population.apply(lambda x: int(x.replace(",", "")))

df_pop["State"].values[:3]

df_pop["State"] = df_pop["State"].apply(lambda x: x.strip())

# df_pop.head()

# df_pop.dtypes

df_pop2 = df_pop.set_index("City")

df_pop2 = df_pop2.sort_index()

df_pop2.head()

df_pop2.head()

df_pop3 = df_pop.set_index(["State", "City"])

df_pop3.head(7)

df_pop3.loc["Sweden"]

df_pop3.loc[("Sweden", "Gothenburg")]

df_pop.set_index("City").sort_values(
    by=["State", "NumericPopulation"], ascending=[False, True]).head()

city_counts = df_pop.State.value_counts()

city_counts.name = "# cities in top 105"

df_pop3 = df_pop[["State", "City", "NumericPopulation"]].set_index([
                                                                   "State", "City"])

df_pop4 = df_pop3.sum(level="State").sort_values(
    "NumericPopulation", ascending=False)

df_pop4.head()

df_pop5 = (df_pop.drop("Rank", axis=1)
                 .groupby("State").sum()
                 .sort_values("NumericPopulation", ascending=False))

df_pop5.head()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

city_counts.plot(kind='barh', ax=ax1)
ax1.set_xlabel("# cities in top 105")
df_pop5.NumericPopulation.plot(kind='barh', ax=ax2)
ax2.set_xlabel("Total pop. in top 105 cities")

fig.tight_layout()
#fig.savefig("state-city-counts-sum.pdf")

"""### Series object - One column DatFrame"""

s = pd.Series([909976, 8615246, 2872086, 2273305])

s

type(s)

s.dtype

s.index

s.values

s.index = ["Stockholm", "London", "Rome", "Paris"]

s.name = "Population"

s

s = pd.Series([909976, 8615246, 2872086, 2273305],
              index=["Stockholm", "London", "Rome", "Paris"], name="Population")

s["London"]

s.Stockholm

s[["Paris", "Rome"]]

s.median(), s.mean(), s.std()

s.min(), s.max()

s.quantile(q=0.25), s.quantile(q=0.5), s.quantile(q=0.75)

s.describe()

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

s.plot(ax=axes[0], kind='line', title="line")
s.plot(ax=axes[1], kind='bar', title="bar")
s.plot(ax=axes[2], kind='box', title="box")
s.plot(ax=axes[3], kind='pie', title="pie")

fig.tight_layout()
fig.savefig("ch12-series-plot.pdf")
fig.savefig("ch12-series-plot.png")
