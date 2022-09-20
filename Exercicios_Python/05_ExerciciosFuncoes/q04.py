'''
Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
'''

def questao04(n):
    return 'P' if n > 0 else 'N'

n = int(input('Digite um numero: '))
resultado = questao04(n)
print(resultado)