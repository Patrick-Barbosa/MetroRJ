# Importar as bibliotecas necess‡rias
import pandas as pd
import numpy as np
from dateutil.holidays import Turkey
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

# Ler o dataset
df = pd.read_excel("dados_passageiros.xlsx")

# Renomear as colunas para ds e y, conforme exigido pela biblioteca Prophet
df = df.rename(columns={"Data": "ds", "Passageiros": "y"})

# Remover os valores vazios
df = df.dropna()

# Criar um modelo Prophet
m = Prophet()

# Treinar o modelo com o dataset
m.fit(df)

# Criar um dataframe para armazenar as datas futuras para a previs‹o
future = m.make_future_dataframe(periods=12, freq="MS")

# Fazer a previs‹o para as datas futuras
forecast = m.predict(future)

# Extrair apenas as colunas ds e yhat (previs‹o) do dataframe forecast
forecast = forecast[["ds", "yhat"]]

# Mostrar as œltimas 12 linhas do dataframe forecast, correspondentes aos 12 meses de previs‹o
print(forecast.tail(12))