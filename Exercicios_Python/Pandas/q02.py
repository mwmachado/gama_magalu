'''
2. Utilizando pandas, realize as seguintes alterações no dataset:
   1. Transforme 20% das notas em valores nulos(None), simulando alunos que não compareceram à prova.
   2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
     `df = df.fillna(0)`
   3. Remova alunos com idades inferiores a 18 e superiores a 80, simulando uma filtragem automática do sistema para alunos com idades incosistentes.
   4. Crie um novo campo aprovado para os alunos restantes que obtiveram nota igual ou superior a 600, com o valor 'Aprovado'. Simulando uma correção automática.
   5. Preencha o resto do campo de aprovado com 'Reprovado' para os demais alunos (preenchimento de nulo).
   `df = df[coluna].fillna('Reprovado')`
   6. Mostre a quantidade de alunos aprovados e reprovados.
'''

import pandas as pd
df = pd.read_csv('enem.csv')


# Parte 1
alunos_faltantes = df.sample(frac=.2, random_state=0).index
#[index, coluna]
df.loc[alunos_faltantes, 'nota'] = None

# Parte 2
df = df.fillna(0)

# Parte 3
menor_18 = df['idade'] < 18 
maior_80 = df['idade'] > 80 #>18 & <80
filtro = ~(menor_18 | maior_80) 
#[index, coluna]
df = df.loc[filtro, :]
print(df.loc[filtro, :])

# Parte 4
maior_600 = df['nota'] > 600
df['aprovado'] = None
df.loc[maior_600, 'aprovado'] = 'Aprovado'
print(df)

# Parte 5
df['aprovado'] = df['aprovado'].fillna('Reprovado')
#df.loc[~maior_600, 'aprovado'] = 'Reprovado'
print(df)

# Parte 6
print(df['aprovado'].value_counts())
#print(df.loc[:, 'aprovado'].value_counts())
filtro_aprovado = df['aprovado'] == 'Aprovado'
print(f"Aprovado: {df.loc[filtro_aprovado, 'aprovado'].count()}")
print(f"Reprovado: {df.loc[~filtro_aprovado, 'aprovado'].count()}")

# Parte 7
df.to_csv('resultado_enem.csv', index=False)