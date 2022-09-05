# Faça um Programa que peça um número correspondente a um determinado ano
#  e em seguida informe se este ano é ou não bissexto.
'''
ano
4 -> bissexto
100 -> não é bissexto
400 -> é bissexto
2000
'''

ano = int(input('Digite o ano: '))
if ano%4 == 0 and ano%100 != 0  or ano%400 == 0:
    #(True and False) or True 
    #False or True
    #True
    print('Ano bissexto')
else:
    print('Ano não bissexto')