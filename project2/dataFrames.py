import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# DataFrame object, different ways to create the same
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
print(df.dtypes, "\n")
print(df.head(),"\n")



## Larger dataset
df_pop = pd.read_csv("european_cities.csv", delimiter=",",encoding='unicode_escape', header=0)

print(df_pop.head(),"\n")
print(df_pop.info(),"\n")
print(df_pop.head(),"\n")

df_pop["NumericPopulation"] = df_pop.Population.apply(lambda x: int(x.replace(",", "")))

print(df_pop["State"].values[:3],)

df_pop["State"] = df_pop["State"].apply(lambda x: x.strip())

print(df_pop.head())
print(df_pop.dtypes,"\n")

df_pop2 = df_pop.set_index("City")

print(df_pop2.head(),"\n")

df_pop2 = df_pop2.sort_index()

print(df_pop2.head(),"\n")

df_pop3 = df_pop.set_index(["State", "City"])

print(df_pop3.head(7),"\n")
print(df_pop3.loc["Sweden"],"\n")
print(df_pop3.loc[("Sweden", "Gothenburg")],"\n")

df_pop.set_index("City").sort_values(by=["State", "NumericPopulation"], ascending=[False, True]).head()

city_counts = df_pop.State.value_counts()

city_counts.name = "# cities in top 105"

df_pop3 = df_pop[["State", "City", "NumericPopulation"]].set_index(["State", "City"])

print(df_pop3.head(),"\n")

df_pop4 = df_pop3.sum(level="State").sort_values("NumericPopulation", ascending=False)

print(df_pop4.head(),"\n")

df_pop5 = (df_pop.drop("Rank", axis=1).groupby("State").sum().sort_values("NumericPopulation", ascending=False))

print(df_pop5.head(), "\n")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

city_counts.plot(kind='barh', ax=ax1)

ax1.set_xlabel("Number cities in top 105")

df_pop5.NumericPopulation.plot(kind='barh', ax=ax2)

ax2.set_xlabel("Total population in top 105 cities")

fig.tight_layout()
fig.savefig("state_city_sum.png")

# Series of object in one column DatFrame
s = pd.Series([909976, 8615246, 2872086, 2273305])

print(s, "\n")
print(type(s), "\n")
print(s.dtype, "\n")
print(s.index, "\n")
print(s.values, "\n")

s.index = ["Stockholm", "London", "Rome", "Paris"]

s.name = "Population"

print(s, "\n")



s = pd.Series([909976, 8615246, 2872086, 2273305],
              index=["Stockholm", "London", "Rome", "Paris"], name="Population")



print(s["London"], "\n")
print(s.Stockholm, "\n")
print(s[["Paris", "Rome"]], "\n")
print(s.median(), s.mean(), s.std(), "\n")
print(s.min(), s.max(), "\n")
print(s.quantile(q=0.25), s.quantile(q=0.5), s.quantile(q=0.75), "\n")
print(s.describe(),"\n")



fig, axes = plt.subplots(1, 4, figsize=(12, 3))
s.plot(ax=axes[0], kind='line', title="line")
s.plot(ax=axes[1], kind='bar', title="bar")
s.plot(ax=axes[2], kind='box', title="box")
s.plot(ax=axes[3], kind='pie', title="pie")

fig.tight_layout()
fig.savefig("graphs.png")

plt.show()
