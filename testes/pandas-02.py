import pandas as pd

df = pd.read_csv("vendas.csv")
print(df.head(1))
print(df.describe())
print(df.info())


df["faturamento"] = df["quantidade"] * df["preco_unitario"]
print(df)

df.groupby("produto")["faturamento"].sum()
print(df)

df[df["preco_unitario"] > 500]

print(df)