# %%
import pandas as pd
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

# %%
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

# %%
quantidade['manteiga']

# %%
quantidade[1:3]

# %%
quantidade.astype(str) + 'g'
# quantidade = quantidade.astype(str)

# %%
quantidade * 1.1

# %%
quantidade.values
quantidade.values.tolist()

# %%
quantidade.index
quantidade.index.tolist()

# %%
quantidade.name

# %%
quantidade.dtype

# %%
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

# %%
df['ingredientes']

# %%
df['quantidades']

# %%
df['medidas'] = 'g'
df

# %%
# [linhas, colunas]
# .loc => localização nome
# .iloc => localização posição
#df['medidas'][3] = 'unidades'
#df.iloc[3, 2] = 'unidades'
df.loc[3, 'medidas'] = 'unidades'
df
# %%
df.columns

# %%
df.index.tolist()

# %%
df.dtypes

# %%
df.info()

# %%
# mostrar os primeiros elementos
df.head(3)

# %%
# mostrar os últimos elementos
df.tail(3)

# %%
df.sample(3)

# %%
df.sample(frac=0.30)

# %%
df.describe()

# %%
#df.sort_values('ingredientes')
#df.sort_values('ingredientes', ascending = False)
#df.sort_values('quantidades', ascending = False)
df.sort_index(ascending=False)

# %% [markdown]
# - not ~
# - and &
# - or  |
# - in isin

# %%
geladeira = [
    'ovos',
    'açucar',
    'maisena'
]

maior_200 = df['quantidades'] > 200
tem_na_geladeira = df['ingredientes'].isin(['ovos', 'açucar', 'maisena'])
filtro = ~tem_na_geladeira & maior_200
df[filtro]

# %%
#max(df['quantidades'])
#df['quantidades'].max()
#df['quantidades'].min()
#df['quantidades'].sum()
#df['quantidades'].mean()
#df['quantidades'].count()

# %%
for ingrediente in df['ingredientes']:
    print(ingrediente)

# %%
df.to_csv('biscoitos.csv', index=False)

# %%
df = pd.read_csv('biscoitos.csv')
df
# %% [markdown]
# Referencia:
# https://pandas.pydata.org/docs/user_guide/10min.html