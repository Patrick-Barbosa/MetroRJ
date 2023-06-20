import pandas as pd

# Lista dos arquivos Excel
arquivos_excel = ['df_linha1_final 98-02.xlsx' ,'df_linha1_final 03-06.xlsx', 'df_linha1_final 07-08.xlsx', 'df_linha1_final 09.xlsx', 
                  'df_linha1_final 07-08.xlsx','df_linha1_final 10-13.xlsx','df_linha1_final 14-15.xlsx', 'df_linha1_final 16-23.xlsx']

# Lista para armazenar os DataFrames
dataframes = []

# Ler cada arquivo e armazenar na lista de DataFrames
for arquivo in arquivos_excel:
    df = pd.read_excel(arquivo, engine='openpyxl')
    dataframes.append(df)

# Concatenar todos os DataFrames
df_concatenado = pd.concat(dataframes, ignore_index=True)

# Salvar o DataFrame concatenado em um novo arquivo Excel
df_concatenado.to_excel('Dataframe.xlsx', index=False, engine='openpyxl')
