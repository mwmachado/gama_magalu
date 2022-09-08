'''
1. gerar uma lista de alunos
1. random, sequeciar (enumerate), 0,1,2,3
1. lista pop (não existe o método pop em tuplas)
1. 4 listas, 1 dicionario
'''

import random

alunos = [
    'Ana Paula Santos',
    'Anderson Teixeira',
    'Beatriz Cardozo',
    'Bruna Rafael',
    'Bruno Carvalho',
    'Bruno fernandes da costa',
    'Bruno Lima',
    'Divino alonso',
    'Edson Almeida',
    'Erick Bontempo',
    'Eron Morais',
    'Ettore Mitsueda',
    'Fernando Araujo Del Lama',
    'Fernando Gava',
    'Fernando S Oliveira',
    'Gabriel Queiroz',
    'Gabriel Silva',
    'Gabrielle Rodrigues',
    'George Lopes Freire',
    'João Paulo Dutra Garcia',
    'José Câmara',
    'José vitor',
    'Julia Guimarães ',
    'Júnior Rodrigues Lopes',
    'Larissa Brito Rodrigues',
    'Lucas Henrique de Oliveira Silva',
    'Lucas Silveira',
    'Maria Clara Rosa ',
    'Osiel Me',
    'Raissa Bangoim Xavier',
    'Sandro Marra',
    'Thiago Cavalcante',
    'Wagner Braz Cambur',
    'Willian Caetano',
    'Willian Ferrari',
]

random.shuffle(alunos)
print(alunos)