# poderia ser uma tupla
alunos = [
    'Ana Paula Santos', #contador
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
    'Ferncontador = 0ielle Rodrigues',
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

'''
chave pesquisa (verbete): numero do grupo
valor a ser retornado (definição): lista alunos
'''

# Eron, Bruno, Anderson
grupo = {}
qtd_grupos = 8
#for chave in range(9):
for chave in range(qtd_grupos): #0,1,2,3,4,5,6,7,8
    # grupo[0] = [] 
    grupo[chave] = []

'''
for chave in 0,1,2,3,4,5,6,7,8:
    dicionario[chave] = valor,
# para cada chave no sequencia de inteiros do zero (incluso) até a quantidade de grupos (excluso,9)
for chave in range(qtd_grupos):

grupo = {
    0:[],
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[]
}
'''

#for linha in range(36):
#tamanho_lista = len(alunos)
#for linha in range(tamanho_lista):
#for linha in range(len(alunos)): #0
'''
for aluno in alunos:
    for chave in 0,1,2,3:
        if len(grupo[chave]) < 5:
            grupo[chave].append(aluno)
            break

print(grupo)
'''

posicao = 0
while posicao < len(alunos):#32
    chave = posicao%qtd_grupos
    grupo[chave].append(alunos[posicao])
    posicao = posicao + 1

print(grupo)