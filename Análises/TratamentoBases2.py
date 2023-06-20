import pandas as pd

# Lendo o arquivo
df = pd.read_excel('Dataframe.xlsx')
df = df.rename(columns={"Linha/Estações": "Estação"})
df_melted = pd.melt(df, id_vars=["Ano", "Estação"], var_name="Mês", value_name="Passageiros")
df_melted.to_excel("dados_passageiros.xlsx", index=False)
