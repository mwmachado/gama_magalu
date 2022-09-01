'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area = float(input('Área a ser pintada (m²): '))
litros = area/3
latas = litros/18
latas_arredondado = round(latas + .49)
preco = latas_arredondado*80

print('Latas de tintas a serem compradas: ', latas_arredondado, 'unidade(s)')
print('Preço total: R$', preco)

''' Testes
area -> esperado
0 -> R$0
30 -> R$80
54 -> R$80
54.01
54.54 -> R$160
'''