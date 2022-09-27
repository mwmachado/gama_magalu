'''
Dados Numéricos:
- [x] A Moda
- [x] A Mediana
- [x] A média
- [x] Os Quartis
- [x] Os 10% maiores
- [x] Os 5 % Menores
- [x] O valor máximo
- [x] O valor mínimo

Dados de Texto
- [x] A frequência absoluta
- [x] A frequência relativa
- [x] A Moda
- [ ] Qual o tipo de Moda?
- [x] O valor máximo (ordem alfabética)
- [x] O valor mínimo (ordem alfabética)
'''

#%%

import pandas as pd
csv = '/home/matheus/Desktop/gama_magalu/Exercicios_Python/Pandas/estatistica_gama.csv'
df = pd.read_csv(csv, decimal=',')
#print(df.info())

numericas = [
    'Idade',
    'Filhos',
    'Altura'
]

'''
for coluna in numericas:
    print()
    print(coluna)

    print(f'Média: {df[coluna].mean()}')
    print(f'Moda: {df[coluna].mode()[0]}')
    print(f'Mediana: {df[coluna].median()}')
    print(f'Mínimo: {df[coluna].min()}')
    print(f'bottom 5%: {df[coluna].quantile(.05)}')
    print(f'Q1: {df[coluna].quantile(.25)}')
    print(f'Q2: {df[coluna].quantile(.5)}')
    print(f'Q3: {df[coluna].quantile(.75)}')
    print(f'top 10%: {df[coluna].quantile(.9)}')
    print(f'Máximo: {df[coluna].max()}')
    #print(f'top 10%: {df[coluna].sort_values().head(3).tolist()}')
    #print(f'bottom 5%: {df[coluna].sort_values().tail(1).tolist()}')
'''

print(df[numericas].describe(percentiles=[.05,.25,.5,.75,.9]))
print(df[numericas].mode())

#%%
'''Correlação
# %%
df[['Idade', 'Filhos']].plot.scatter(x="Idade", y="Filhos")

# %%
df[['Idade', 'Filhos']].corr()
# abaixo .5 não tem correlação ou correlação fraca
# entre .5 .75 tem correlação moderada
# .75 tem correlação forte
'''
#%%
texto = [
    'Nome',
    'Estado',
    'Formação'
]

def tipo_moda(serie):
    qtd = len(serie.mode()) #.shape
    if qtd == 0:
        return 'Sem Moda'
    elif qtd == 1:
        return 'Unimodal'
    elif qtd == 2:
        return 'Bimodal'
    elif qtd > 2:
        return 'Multimodal'
    else:
        return 'Valor inválido'

for col in texto:
    df[col] = df[col].str.lower() # passa tudo para minúsculo
    df[col] = df[col].str.strip() # remove espaços em branco no começo ou final
    print()
    print(col)
    print(f'Frequência Absoluta: ')
    print(f'{df[col].value_counts()}')
    print()
    print(f'Frequência Relativa: ')
    print(f'{df[col].value_counts(normalize=True)}')
    print()
    print(f'Moda: {df[col].mode()[0]}')
    print(f'Mínimo: {df[col].min()}')
    print(f'Máximo: {df[col].max()}')
    print(f'Tipo de Moda: {tipo_moda(df[col])}')

print(df[texto].describe())