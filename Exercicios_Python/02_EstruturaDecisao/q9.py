# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input('Preço Produto 1:'))
n2 = float(input('Preço Produto 2:'))
n3 = float(input('Preço Produto 3:'))

print('Segue os números em ordem descrescente:')
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

if n1 != maior and n1 != menor:
    meio = n1
elif n2 != maior and n2 != menor:
    meio = n2
else:
    meio = n3

print(maior, meio, menor, sep=',')