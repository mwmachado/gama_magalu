# 2. Crie um array de duas dimensões, no formato 9x9, com números de 0 a 80 ordenados de modo crescente e selecione:
#    1. Os números ímpares
#    2. Os números pares
#    3. Os múltiplos de sete
#    4. Os múltiplos de 10
#    5. Os números 32,33,42,43

# Criação do array
import numpy as np
array = np.arange(81)
array = array.reshape([9,9])
array

# Item 1
impares = array%2 == 1 #máscara de números impares
print()
print('1. Os números ímpares:')
print(array[impares])
#[1:] caso queira remover o 0

# Item 2
# np.invert(impares) not impar
pares = array%2 == 0 #máscara de números pares
print()
print('2. Os números pares:')
print(array[pares])
#[1:] caso queira remover o 0

# Item 3
mult_7 = array%7 == 0 #multiplos de 7
print()
print('3. Os múltiplos de sete:')
print(array[mult_7])

# Item 4
#mult_10 = array%10 == 0
print()
print('4. Os múltiplos de 10:')
print(array.diagonal()) # multiplos de 10

# Item 5
linhas = [3,3,4,4]
colunas = [5,6,6,7]
print()
print('5. Os números 32,33,42,43:')
print(array[linhas,colunas])


