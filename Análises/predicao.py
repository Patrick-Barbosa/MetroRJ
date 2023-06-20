# Importar as bibliotecas necess√°rias
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Ler os dados do arquivo Excel
dados = pd.read_excel("dados_passageiros.xlsx")

# Remover os valores vazios
dados = dados.dropna()

# Converter a coluna Data em formato datetime
dados["Data"] = pd.to_datetime(dados["Data"])

# Extrair o ano e o MÍs da coluna Data
dados["Ano"] = dados["Data"].dt.year
dados["MÍs"] = dados["Data"].dt.month

# Agrupar os dados por ano e MÍs e calcular a soma dos passageiros por EstaÁ„o
dados_agrupados = dados.groupby(["Ano", "MÍs", "EstaÁ„o"])["Passageiros"].sum().reset_index()

# Criar uma coluna com o n√∫mero do MÍs (de 1 a 12)
dados_agrupados["MÍs_num"] = (dados_agrupados["Ano"] - 1998) * 12 + dados_agrupados["MÍs"]

# Separar os dados em vari√°veis independentes (X) e dependente (y)
X = dados_agrupados[["MÍs_num", "EstaÁ„o"]]
y = dados_agrupados["Passageiros"]

# Codificar a vari√°vel categ√≥rica EstaÁ„o usando o m√©todo get_dummies
X = pd.get_dummies(X, columns=["EstaÁ„o"])

# Criar um modelo de regress√£o linear
modelo = LinearRegression()

# Treinar o modelo com os dados
modelo.fit(X, y)

# Criar um dataframe com os valores de MÍs_num e EstaÁ„o para 2024
meses = np.arange(313, 325) # de janeiro a dezembro de 2024
estacoes = dados["EstaÁ„o"].unique()
X_pred = pd.DataFrame({"MÍs_num": np.repeat(meses, len(estacoes)), "EstaÁ„o": np.tile(estacoes, len(meses))})

# Codificar a vari√°vel categ√≥rica EstaÁ„o usando o m√©todo get_dummies
X_pred = pd.get_dummies(X_pred, columns=["EstaÁ„o"])


# Fazer a predi√ß√£o usando o modelo treinado
y_pred = modelo.predict(X_pred)

# Adicionar a coluna de predi√ß√£o ao dataframe
X_pred["Passageiros"] = y_pred

# Mostrar o resultado
print(X_pred)


# Criar uma lista com os nomes dos meses
nomes_meses = ["Janeiro", "Fevereiro", "Mar√ßo", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Adicionar uma coluna com os nomes dos meses ao dataframe X_pred
X_pred["MÍs"] = X_pred["MÍs_num"].apply(lambda x: nomes_meses[x % 12 - 1])

# Mostrar o resultado
print(X_pred)

# Remover a coluna MÍs_num, que n√£o √© necess√°ria para a visualiza√ß√£o
X_pred = X_pred.drop(columns=["MÍs_num"])

# Reverter o m√©todo get_dummies, criando uma coluna EstaÁ„o com as categorias originais
X_pred["EstaÁ„o"] = X_pred.iloc[:, 0:19].idxmax(axis=1).str.replace("EstaÁ„o_", "")

# Remover as colunas bin√°rias criadas pelo m√©todo get_dummies
X_pred = X_pred.drop(columns=X_pred.columns[0:19])

# Reordenar as colunas para colocar a coluna EstaÁ„o antes da coluna Passageiros
X_pred = X_pred[["MÍs", "EstaÁ„o", "Passageiros"]]

# Arredondar os valores da coluna Passageiros para duas casas decimais
X_pred["Passageiros"] = X_pred["Passageiros"].round(2)

# Mostrar o resultado
print(X_pred)
















# Importar pandas para ler o arquivo Excel
import pandas as pd

# Ler o arquivo Excel e armazenar em um DataFrame
df = pd.read_excel("dados_passageiros.xlsx")

# Agrupar os dados por ano e calcular a m√©dia na coluna Passageiros
media_por_ano = df.groupby("Ano")["Passageiros"].mean()

# Imprimir a m√©dia por ano
print("A m√©dia de passageiros por ano √©:")
print(media_por_ano)