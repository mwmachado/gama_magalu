'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

n = int(input('N: '))
def questao01(n):
    for linha in range(1, n+1):
        print((str(linha)+ ' ') * linha)

questao01(n)

'''
i = 1 # contador
while i <= n:
    print((str(linha)+ ' ') * linha) # repeticao
    i = i+1 #incremento
'''
'''
#1 ate 11(não incluso)
vezes = int(input('N:')) #10
for numero in range(1, vezes+1):
    #numero='4'
    #print(('3'+' ')*3)
    print((str(numero)+' ')*numero)
    #print((numero+' ')*int(numero))
'''