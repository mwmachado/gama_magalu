# %% Importação da biblioteca
import pandas as pd

# %% Criação da séries de ingredientes
ingredientes = [
    'maisena',
    'farinha',
    'açucar',
    'ovos',
    'manteiga',
    'castanhas'
]

serie = pd.Series(ingredientes, name='ingredientes', dtype=object)
serie

# %% Criação da série de quantidades
qtd = [
    200,
    250,
    100,
    2,
    150,
    180
]

quantidade = pd.Series(qtd, index=ingredientes, name='quantidades')
quantidade

# %% Seleção por index
quantidade['manteiga']

# %% Seleção por posição
quantidade[1:3]

# %% Transformação de tipo de série
quantidade.astype(str) + 'g'
# quantidade = quantidade.astype(str)

# %% Operações Matemáticas com séries
quantidade * 1.1

# %% Valores da série
quantidade.values
quantidade.values.tolist()

# %% Index da série
quantidade.index
quantidade.index.tolist()

# %% Nome da série
quantidade.name

# %% Tipo de dado da série
quantidade.dtype

# %% Criação de DataFrame
'''
{
    coluna1 : valores_coluna1,
    coluna2 : valores_coluna2
}
'''
df = pd.DataFrame({
    'ingredientes': ['maisena','farinha','açucar','ovos','manteiga','castanhas'],
    'quantidades': [200,250,100,2,150,180]
})
df

# %% Seleção da coluna de ingredientes
df['ingredientes']

# %% Seleção da coluna de quantidades
df['quantidades']

# %% Criação de coluna com apenas um valor
df['medidas'] = 'g'
df

# %% Seleção de célula e atribução de valor
# [linhas, colunas]
# .loc => localização nome
# .iloc => localização posição
#df['medidas'][3] = 'unidades'
#df.iloc[3, 2] = 'unidades'
df.loc[3, 'medidas'] = 'unidades'
df
# %% Colunas do DataFrame
df.columns

# %% Índice do DataFrame
df.index.tolist()

# %% Tipos das colunas do DataFrame
df.dtypes

# %% Informações do DataFrame
df.info()

# %% Primeiros elementos
df.head(3)

# %% Últimos elementos
df.tail(3)

# %% Amostra de 3 elementos aleatórios
df.sample(3)

# %% Amostra de 30% dos elementos
df.sample(frac=0.30)

# %% Estatísticas do DataFrame
df.describe()

# %% Ordenação dos valores ou index
#df.sort_values('ingredientes')
#df.sort_values('ingredientes', ascending = False)
#df.sort_values('quantidades', ascending = False)
df.sort_index(ascending=False)

# %% Operações booleanas para Séries, Arrays, e DataFrames
# - not ~
# - and &
# - or  |
# - in isin

# %% Filtros concatenados
geladeira = [
    'ovos',
    'açucar',
    'maisena'
]

maior_200 = df['quantidades'] > 200
tem_na_geladeira = df['ingredientes'].isin(['ovos', 'açucar', 'maisena'])
filtro = ~tem_na_geladeira & maior_200
df[filtro]

# %% Funções comuns
#max(df['quantidades'])
#df['quantidades'].max()
#df['quantidades'].min()
#df['quantidades'].sum()
#df['quantidades'].mean()
#df['quantidades'].count()

# %% Iteração sobre o dataframe
for ingrediente in df['ingredientes']:
    print(ingrediente)

# %% Salvar DataFrame em arquivo CSV
df.to_csv('biscoitos.csv', index=False)

# %% Ler DataFrame de Arquivo CSV
df = pd.read_csv('biscoitos.csv')
df

# %% Referencia:
# https://pandas.pydata.org/docs/user_guide/10min.html