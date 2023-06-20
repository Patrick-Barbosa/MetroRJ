import pandas as pd

# Carrega os dados em um DataFrame
df= pd.read_excel('dataframe.xlsx')

# Remove a coluna de Ano
df.drop('Ano', axis=1, inplace=True)

# Calcula o desvio padrão para cada estação
stds = df.std(axis=1)

# Identifica a estação com o maior desvio padrão
max_std_station = df.loc[stds.idxmax(), 'Linha/Estações']

# Imprime aação com o maior desvio padrão
print(f'A estação com o maior desvio padrão é: {max_std_station}')


import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados em um DataFrame
df = pd.read_excel('Dataframe.xlsx')

# Remove os anos 2020 e 2021
df = df[(df['Ano'] != 2020) & (df['Ano'] != 2021)]

# Seleciona apenas os dados da estação de Triagem
df_triagem = df[df['Linha/Estações'] == 'Triagem']

# Cria um gráfico de linha para a estação de Triagem
for index, row in df_triagem.iterrows():
    plt.plot(df_triagem.columns[2:], row[2:], label=row['Ano'])

plt.title('Valores da Estação de Triagem (excluindo 2020 e 2021)')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.legend()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados em um DataFrame
df = pd.read_excel('Dataframe.xlsx')

# Remove os anos 2020 e 2021
df = df[(df['Ano'] != 2020) & (df['Ano'] != 2021)]

# Seleciona apenas os dados da estação de Triagem
df_triagem = df[df['Linha/Estações'] == 'Triagem']

# Calcula a média dos valores mensais
df_triagem['Média'] = df_triagem.iloc[:, 2:].mean(axis=1)

# Cria um gráfico de linha para a estação de Triagem
plt.plot(df_triagem['Ano'], df_triagem['Média'])
plt.title('Média dos Valores Mensais da Estação de Triagem (excluindo 2020 e 2021)')
plt.xlabel('Ano')
plt.ylabel('Média dos Valores Mensais')
plt.show()
