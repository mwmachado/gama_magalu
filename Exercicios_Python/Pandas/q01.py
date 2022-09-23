'''
1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
   1. Idade: números inteiros aleatórios entre 0 e 100 (inclusos).
   2. Nota: Números decimais entre 0 e 1000.
   3. Sexo: Valores aleatórios de M ou F
   4. Estado: Valores aleatórios entre os estados do Brasil.
'''
# Bibliotecas
import numpy as np
import pandas as pd

opcoes_sexo = ['M', 'F']
estados = [
    'AC','AL','AP',
    'AM','BA','CE',
    'ES','GO','MA',
    'MT','MS','MG',
    'PA','PB','PR',
    'PE','PI','RJ',
    'RN','RS','RO',
    'RR','SC','SP',
    'SE','TO','DF'
]

turma = pd.DataFrame({
    'idade' : np.random.randint(low=1,high=101,size=1000),
    'nota' : np.random.uniform(low=0, high=1001, size=1000),
    'sexo' : np.random.choice(opcoes_sexo,size=1000),
    'estado' : np.random.choice(estados,size=1000),
})

turma.to_csv('enem.csv', index=False)








'''
# Idade com numpy
np.random.randint(0, 101, size=[1000])

# Idade lista
import random
idade = []
for i in range(1000):
    idade.append(random.randint(0,100))

idade

# sexos = ['M', 'F']
np.random.choice(sexos, 1000)

# estados = [
  'AC', 'AL', 'AP',
  'AM', 'BA', 'CE',
  'ES', 'GO', 'MA',
  'MT', 'MS', 'MG',
  'PA', 'PB', 'PR',
  'PE', 'PI', 'RJ',
  'RN', 'RS', 'RO',
  'RR', 'SC', 'SP',
  'SE', 'TO', 'DF',
]

#np.random.choice(estados, 1000)

# np.random.rand(1000) * 1000

df = pd.DataFrame({
    'idade': np.random.randint(0, 101, size=[1000]),
    'nota': np.random.rand(1000) * 1000,
    'sexo': np.random.choice(sexos, 1000),
    'estado': np.random.choice(estados, 1000)
})

df.to_csv('enem.csv', index=False)
'''