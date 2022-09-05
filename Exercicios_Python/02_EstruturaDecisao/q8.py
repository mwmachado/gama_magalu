# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.
n1 = float(input('Preço Produto 1:'))
n2 = float(input('Preço Produto 2:'))
n3 = float(input('Preço Produto 3:'))

menor_valor = min(n1, n2, n3)

print('Compre o produto', end=' ')
if n1 == menor_valor:
    print('Produto 1')
elif n2 == menor_valor:
    print('Produto 2')
else:
    print('Produto 3')