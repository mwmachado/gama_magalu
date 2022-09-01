'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

n1 = int(input('1° número (int): '))
n2 = int(input('2° número (int): '))
n3 = float(input('3° número (real): '))

print('a) o produto do dobro do primeiro com metade do segundo .: ', (n1*2)*(n2*.5))
print('b) a soma do triplo do primeiro com o terceiro.: ', (n1*3)+n3)
print('c) o terceiro elevado ao cubo.: ', n3**3)