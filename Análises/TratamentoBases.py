import pandas as pd
import numpy as np

anos = ['1998', '1999', '2000', '2001', '2002']
dfLinha1 = []
dfLinha2 = []

for ano in anos:
    df = pd.read_excel('total-mensal-passageiros.xlsx', sheet_name=ano, header=5)
    
    df_linha1 = df.loc[5:20]
    df_linha1.insert(0, 'Ano', ano)
    df_linha1 = df_linha1.set_index(df_linha1.columns[0])
    df_linha1 = df_linha1.replace('...', np.nan)

    
    df_linha2 = df.loc[24:38]
    df_linha2.insert(0, 'Ano', ano)
    df_linha2 = df_linha2.set_index(df_linha2.columns[0])
    df_linha2 = df_linha2.replace('...', np.nan)
    
    dfLinha1.append([df_linha1])
    dfLinha2.append([df_linha2])

# Concatena todos os DataFrames em um único DataFrame
df_Final1 = pd.concat([pd.concat(dfs) for dfs in dfLinha1], ignore_index=True)
df_Final2 = pd.concat([pd.concat(dfs) for dfs in dfLinha2], ignore_index=True)




df = pd.read_excel('total-mensal-passageiros.xlsx', sheet_name='2015', header=5)







import pandas as pd
import numpy as np

anos = ['2014', '2015']
dfLinha1 = []
dfLinha2 = []

for ano in anos:
    df = pd.read_excel('total-mensal-passageiros.xlsx', sheet_name=ano, header=5)
    
    df_linha1 = df.loc[5:24]
    df_linha1.insert(0, 'Ano', ano)
    df_linha1 = df_linha1.replace('...', np.nan)

    df_linha2 = df.loc[28:43]
    df_linha2.insert(0, 'Ano', ano)
    df_linha2 = df_linha2.replace('...', np.nan)
        
    dfLinha1.append(df_linha1)
    dfLinha2.append(df_linha2)

# Concatena todos os DataFrames em um único DataFrame
df_linha1_final = pd.concat(dfLinha1, ignore_index=True)
df_linha2_final = pd.concat(dfLinha2, ignore_index=True)


df_linha1_final = df_linha1_final.set_index(df_linha1_final.columns[0])
df_linha2_final = df_linha2_final.set_index(df_linha2_final.columns[0])


df_linha1_final.to_excel('df_linha1_final 14-15.xlsx', index=True)
df_linha2_final.to_excel('df_linha2_final 14-15.xlsx', index=True)




























import pandas as pd
import numpy as np

anos = ['2016', '2017','2018', '2019', '2020', '2021', '2022', '2023']
dfLinha1 = []
dfLinha2 = []
dfLinha4 = []

for ano in anos:
    df = pd.read_excel('total-mensal-passageiros.xlsx', sheet_name=ano, header=5)
    
    df_linha1 = df.loc[5:24]
    df_linha1.insert(0, 'Ano', ano)
    df_linha1 = df_linha1.replace('...', np.nan)

    df_linha2 = df.loc[28:43]
    df_linha2.insert(0, 'Ano', ano)
    df_linha2 = df_linha2.replace('...', np.nan)
    
    df_linha4 = df.loc[47:51]
    df_linha4.insert(0, 'Ano', ano)
    df_linha4 = df_linha4.replace('...', np.nan)
    
    
    
    dfLinha1.append(df_linha1)
    dfLinha2.append(df_linha2)
    dfLinha4.append(df_linha4)

# Concatena todos os DataFrames em um único DataFrame
df_linha1_final = pd.concat(dfLinha1, ignore_index=True)
df_linha2_final = pd.concat(dfLinha2, ignore_index=True)
df_linha4_final = pd.concat(dfLinha4, ignore_index=True)


df_linha1_final = df_linha1_final.set_index(df_linha1_final.columns[0])
df_linha2_final = df_linha2_final.set_index(df_linha2_final.columns[0])
df_linha4_final = df_linha4_final.set_index(df_linha4_final.columns[0])


df_linha1_final.to_excel('df_linha1_final 16-23.xlsx', index=True)
df_linha2_final.to_excel('df_linha2_final 16-23.xlsx', index=True)
df_linha4_final.to_excel('df_linha4_final 16-23.xlsx', index=True)



print(df_linha1_final)























# df = pd.read_excel('total-mensal-passageiros.xlsx')
df = pd.read_excel('total-mensal-passageiros.xlsx', header=5)

df = pd.read_excel('total-mensal-passageiros.xlsx', sheet_name='1998', header=5)

# Seleciona apenas as linhas que correspondem aos índices de 24 a 38
df_linha2 = df.loc[24:38]
df_linha1 = df.loc[5:20]

df_linha1.insert(0, 'Ano', 1998)
df_linha2.insert(0, 'Ano', 1998)


# Define a primeira coluna como índice do DataFrame
df_linha1 = df_linha1.set_index(df_linha1.columns[0])
df_linha2 = df_linha2.set_index(df_linha2.columns[0])



# Exibe o DataFrame resultante
print(df_linha1)

# Substitui os valores com "..." por NaN
df_linha1 = df_linha1.replace('...', np.nan)
df_linha2 = df_linha2.replace('...', np.nan)


# Exibe o DataFrame resultante
print(df)

