'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

parada = int(input('N: '))
def questao02(parada):
    numero = 1
    texto = str(numero)
    print(texto)

    while numero < parada:
        numero = numero + 1
        texto = texto + ' ' + str(numero)
        print(texto)

questao02(parada)