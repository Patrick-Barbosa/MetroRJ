# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Ler os dados do arquivo Excel
dados = pd.read_excel("dados_passageiros.xlsx")

# Remover os valores vazios
dados = dados.dropna()

# Converter a coluna Data em formato datetime
dados["Data"] = pd.to_datetime(dados["Data"])

# Extrair o ano e o M�s da coluna Data
dados["Ano"] = dados["Data"].dt.year
dados["M�s"] = dados["Data"].dt.month

# Agrupar os dados por ano e M�s e calcular a soma dos passageiros por Esta��o
dados_agrupados = dados.groupby(["Ano", "M�s", "Esta��o"])["Passageiros"].sum().reset_index()

# Criar uma coluna com o número do M�s (de 1 a 12)
dados_agrupados["M�s_num"] = (dados_agrupados["Ano"] - 1998) * 12 + dados_agrupados["M�s"]

# Separar os dados em variáveis independentes (X) e dependente (y)
X = dados_agrupados[["M�s_num", "Esta��o"]]
y = dados_agrupados["Passageiros"]

# Codificar a variável categórica Esta��o usando o método get_dummies
X = pd.get_dummies(X, columns=["Esta��o"])

# Criar um modelo de regressão linear
modelo = LinearRegression()

# Treinar o modelo com os dados
modelo.fit(X, y)

# Criar um dataframe com os valores de M�s_num e Esta��o para 2024
meses = np.arange(313, 325) # de janeiro a dezembro de 2024
estacoes = dados["Esta��o"].unique()
X_pred = pd.DataFrame({"M�s_num": np.repeat(meses, len(estacoes)), "Esta��o": np.tile(estacoes, len(meses))})

# Codificar a variável categórica Esta��o usando o método get_dummies
X_pred = pd.get_dummies(X_pred, columns=["Esta��o"])


# Fazer a predição usando o modelo treinado
y_pred = modelo.predict(X_pred)

# Adicionar a coluna de predição ao dataframe
X_pred["Passageiros"] = y_pred

# Mostrar o resultado
print(X_pred)


# Criar uma lista com os nomes dos meses
nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Adicionar uma coluna com os nomes dos meses ao dataframe X_pred
X_pred["M�s"] = X_pred["M�s_num"].apply(lambda x: nomes_meses[x % 12 - 1])

# Mostrar o resultado
print(X_pred)

# Remover a coluna M�s_num, que não é necessária para a visualização
X_pred = X_pred.drop(columns=["M�s_num"])

# Reverter o método get_dummies, criando uma coluna Esta��o com as categorias originais
X_pred["Esta��o"] = X_pred.iloc[:, 0:19].idxmax(axis=1).str.replace("Esta��o_", "")

# Remover as colunas binárias criadas pelo método get_dummies
X_pred = X_pred.drop(columns=X_pred.columns[0:19])

# Reordenar as colunas para colocar a coluna Esta��o antes da coluna Passageiros
X_pred = X_pred[["M�s", "Esta��o", "Passageiros"]]

# Arredondar os valores da coluna Passageiros para duas casas decimais
X_pred["Passageiros"] = X_pred["Passageiros"].round(2)

# Mostrar o resultado
print(X_pred)
















# Importar pandas para ler o arquivo Excel
import pandas as pd

# Ler o arquivo Excel e armazenar em um DataFrame
df = pd.read_excel("dados_passageiros.xlsx")

# Agrupar os dados por ano e calcular a média na coluna Passageiros
media_por_ano = df.groupby("Ano")["Passageiros"].mean()

# Imprimir a média por ano
print("A média de passageiros por ano é:")
print(media_por_ano)