'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
'''
h = float(input('Altura: '))
peso_homem = (72.7*h) - 58
peso_mulher = (62.1*h) - 44.7

print('a) Para homens: ', round(peso_homem, 2))
print('b) Para mulheres: ', round(peso_mulher, 2))