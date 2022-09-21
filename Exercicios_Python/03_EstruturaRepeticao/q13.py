'''
Faça um programa que peça dois números, base e expoente, calcule
e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''
#base**expoente
#pow(base, expoente)

'''
2³ = 2 * 2 * 2 = 8

1 * 2 = 2
2 * 2 = 4
2 * 2 = 8
'''

base = int(input('Base: '))
expoente = int(input('Expoente: '))
resultado = 1

for passo in range(expoente): #passo 0, passo 1, passo 2
    resultado = resultado * base

print(f'O resultado é {resultado}')