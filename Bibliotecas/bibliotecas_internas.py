'''
import os # comandos de sistema
os.system('clear') # limpa a tela
print(os.getcwd()) #caminho do arquivo que está sendo executado 
def limpa_tela():
    if os.name == 'nt': #windows
        os.system('cls')
    else: #posix
        os.system('clear')

import sys
sys.executable # caminho do executável do python
sys.version # versão do python que está executando

import json
texto = {
    "arroz":10.50,
    "feijao":4
}
dicionario = {'arroz': 10.5, 'feijao': 4}

# texto para dicionario
#str(dicionario) # não faça isso
json.dumps(dicionario) # faça isso

# dicionario para texto
# dict(texto) # não funciona
dicionario = json.loads(texto) #faça isso

from getpass import getpass
#input('Password: ') # não faça isso
getpass('Password: ') # faça isso

from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('Feliz Ano Novo!!!')
'''
from random import randint, sample
from time import sleep
'''
for i in range(10, 0, -1):
    print(randint(1,10))
    sleep(1)
print('Feliz Ano Novo!!!')
'''

lista = [1,2,3,4,5,6,7,8,9,10]
for i in sample(lista, 10):
    print(i)
    sleep(1)
print('Feliz Ano Novo!!!')


