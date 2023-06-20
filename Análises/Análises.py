import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo Excel
df = pd.read_excel('Dataframe.xlsx', engine='openpyxl')

# Calcular a média de passageiros por mês em cada estação
media_passageiros = df.groupby('Linha/Estações').mean().drop('Ano', axis=1)

# Estação com maior movimento
estacao_maior_movimento = media_passageiros.mean(axis=1).idxmax()
media_maior_movimento = media_passageiros.mean(axis=1).max()

# Estação com menor movimento
estacao_menor_movimento = media_passageiros.mean(axis=1).idxmin()
media_menor_movimento = media_passageiros.mean(axis=1).min()

print(f"Estação com maior movimento: {estacao_maior_movimento} (média: {media_maior_movimento:.2f} passageiros/mês)")
print(f"Estação com menor movimento: {estacao_menor_movimento} (média: {media_menor_movimento:.2f} passageiros/mês)")

# Criar um gráfico de barras
media_passageiros['Média Anual'] = media_passageiros.mean(axis=1)
media_passageiros_sorted = media_passageiros.sort_values('Média Anual', ascending=False)
media_passageiros_sorted['Média Anual'].plot(kind='bar', figsize=(15, 6))

# Configurar o gráfico
plt.title('Média de Passageiros por Mês em Cada Estação (1998-2023)')
plt.xlabel('Linha/Estações')
plt.ylabel('Média de Passageiros por Mês')
plt.xticks(rotation=90)

# Mostrar o gráfico
plt.show()

############################################################################

# Ler o arquivo Excel
df = pd.read_excel('Dataframe.xlsx', engine='openpyxl')

# Tratamento da base
df = df.drop(df.columns[[0, 1]], axis=1)

# Obter os nomes dos meses a partir dos cabeçalhos 
meses = df.columns[0:]

# Calcular a média de passageiros por mês considerando todas as estações 
media_mensal = df[meses].mean()

# Criar um DataFrame com os meses e as médias
df_media_mensal = pd.DataFrame({'Mes': meses, 'Media': media_mensal})

# Ordenar do maior para o menor 
df_media_mensal_sorted = df_media_mensal.sort_values(by='Media', ascending=False)

# Mostrar os 5 meses com maior movimento
print(df_media_mensal_sorted.head())

# Criar um gráfico de barras
df_media_mensal_sorted.plot(kind='bar', x='Mes', y='Media', figsize=(10, 6), rot=0)
plt.title('Meses com Maior Movimento de Passageiros')
plt.xlabel('Mês')
plt.ylabel('Média de Passageiros')

# Mostrar o gráfico
plt.show()


############################################################################


# Ler o arquivo Excel
df = pd.read_excel('Dataframe.xlsx', engine='openpyxl')

# Agrupar as estações por linha 
df_por_linha = df.groupby('Linha/Estações')

# Calcular a média total de passageiros em cada linha
media_por_linha = df_por_linha.mean().drop('Ano', axis=1)

# Ordenar do maior para o menor
media_por_linha_sorted = media_por_linha.sort_values(by=list(media_por_linha.columns), ascending=False)

# Mostrar as 3 linhas com maior movimento
print(media_por_linha_sorted.head(3))

# Criar um gráfico de barras 
media_por_linha_sorted.plot(kind='bar', figsize=(27, 6))

# Configurar o gráfico
plt.title('Média de Passageiros por Linha do Metrô')
plt.xlabel('Linha')
plt.ylabel('Média de Passageiros por Mês')
plt.xticks(rotation=0)

# Mostrar o gráfico
plt.show()





