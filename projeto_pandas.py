import pandas as pd
import matplotlib.pyplot as plt
dataf = pd.read_csv("vendas_projeto.csv")

dataf["faturamento"] = dataf["quantidade"] * dataf["preco"]

faturamento_total = dataf["faturamento"].sum()
print(f"\nFaturamento Total: R$ {faturamento_total:.2f}")

produto_mais_vendido = dataf.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
top_produto = produto_mais_vendido.idxmax()
print(f"Produto mais vendido: {top_produto}")

faturamento_por_categoria = dataf.groupby("categoria")["faturamento"].sum()
print("Faturamento por categoria:")
print(faturamento_por_categoria)

dataf["data"] = pd.to_datetime(dataf["data"])
dataf["mes"] = dataf["data"].dt.month

vendas_mes = dataf.groupby("mes")["faturamento"].sum()

vendas_mes.plot(kind="bar")
plt.title("Faturamento por Mês")
plt.xlabel("Mês")
plt.ylabel("Faturamento")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("faturamento_por_mes.png")
plt.show()