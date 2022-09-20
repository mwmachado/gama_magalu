'''
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem
e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

def somaImposto(taxaImposto, custo):
    custo = custo + custo*taxaImposto
    return custo

imposto = float(input('Taxa Imposto (%): '))/100
custo = float(input('Custo (R$): '))

custo = somaImposto(imposto, custo)
print('O novo custo é: R$', custo)