'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
  e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais.
  Informe ao usuário e encerre o programa;
- Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
  informe-a ao usuário;
- Se o delta for positivo, a equação possui duas raiz reais;
  informe-as ao usuário;
'''

import math

print('Dada a equação ax²+bx+c informe os valores abaixo para o cálculo das raízes.')
a = float(input('Informe o valor de a: '))
if a == 0:
  print('A equação não é de segundo grau')
else:
  b = float(input('Informe o valor de b: '))
  c = float(input('Informe o valor de c: '))
  delta = b**2-4*a*c
  if delta < 0:
    print('A equação não possui raízes reais')
  elif delta == 0:
    print('A equação possui apenas uma raiz real')
    print(f'X = {-b/(2*a)}')
  else:
    print('A equação possui duas raizes reais')
    print(f"X' = {(-b+math.sqrt(delta))/(2*a)}")
    print(f'X" = {(-b-math.sqrt(delta))/(2*a)}')

print('Programa encerrado')