
# Resumo breve das análises

Neste projeto, eu usei a biblioteca Prophet para fazer previsões de passageiros em diferentes estações de metrô. O objetivo era estimar o número de passageiros para os próximos 12 meses a partir de abril de 2023, usando os dados históricos de janeiro de 2019 a março de 2023. Para isso, eu realizei várias análises nessa pasta, como tratar a base, concatenar ela, remover valores vazios e afins. Vou tentar resumir ao longo do texto como eu fiz cada etapa.

## Dados

Os dados utilizados neste projeto foram obtidos de um arquivo Excel que continha o número de passageiros por data e estação. O arquivo tinha as seguintes colunas:

- `Data`: a data no formato AAAA-MM-DD
- `Estação`: o nome da estação de metrô
- `Passageiros`: o número de passageiros naquela data e estação

O arquivo tinha 1470 linhas e 3 colunas. Os dados cobriam um período de 51 meses e 6 estações diferentes.

## Análises

Além das previsões, utilizando Prophet, eu também fiz algumas análises estatísticas sobre os dados, tais como:

1. A média de passageiros por estação, usando a função `groupby` do pandas e o método `mean`.
2. O desvio padrão de passageiros por mês, usando a função `groupby` do pandas e o método `std`.
3. O crescimento percentual de passageiros por estação entre o primeiro e o último mês do conjunto de dados, usando a função `groupby` do pandas e o método `pct_change`.
4. A correlação entre o número de passageiros e o mês do ano para cada estação, usando a função `groupby` do pandas e o método `corr`.
5. O coeficiente de determinação (R2) da regressão linear entre o número de passageiros e o mês do ano para cada estação, usando a função `linregress` do scipy.stats.

## Procedimento

Para fazer as previsões, eu segui os seguintes passos:

1. Carreguei o arquivo XLXS usando a função `pandas.read_excel()` do pandas.
2. Removi os valores vazios usando a função `dropna` do pandas.
3. Renomeei as colunas para `ds`, `y` e `group`, que são os nomes exigidos pelo Prophet.
4. Criei e ajustei um modelo Prophet para cada estação, usando um loop for e a função `Prophet` do fbprophet.
5. Fiz previsões para 12 meses a partir de abril de 2023, usando a função `make_future_dataframe` do Prophet e a função `predict` do modelo.
6. Calculei o erro absoluto médio (MAE) para cada estação, usando a função `mean_absolute_error` do sklearn.metrics.
7. Plotei os gráficos das previsões para cada estação, usando a função `plot` do modelo e a função `add_changepoints_to_plot` do Prophet.
8. Exportei o resultado final para um arquivo Excel, usando a função `to_excel` do pandas.

## Conclusão

Neste projeto, eu usei uma ferramenta chamada Prophet para tentar prever quantos passageiros iriam usar diferentes estações de metrô no futuro. Eu descobri que as estações não eram todas iguais e que algumas mudavam mais do que outras ao longo do ano. Eu também calculei o quanto eu podia errar nas minhas adivinhações e achei que era um valor aceitável para o tamanho dos dados. Eu fiz uns desenhos para mostrar como as estações se comportavam e quais eram os momentos mais importantes para elas. Eu salvei tudo isso em um arquivo Excel para cada estação. No entanto, os estudos não foram conclusivos porque ainda há muitas coisas que podem influenciar o número de passageiros.


Espero que este projeto tenha sido interessante e útil. Obrigado pela atenção!