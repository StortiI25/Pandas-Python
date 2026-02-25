import pandas as pd

dados = {
    'produtos': ["Notebook","Mouse","Teclado"],
    'perco':[3500, 80, 150],
    'quantidade':[1, 3, 5]
}

df = pd.DataFrame(dados)
print(df)

