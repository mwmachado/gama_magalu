'''
Supondo que a população de um país A seja da ordem de 80.000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento.
'''

pais_a = 8e4
tx_a = 0.03
pais_b = 2e5
tx_b = 0.015

ano = 0 #simular a passagem de anos
while not (pais_a >= pais_b):
#while pais_a < pais_b:
    pais_a = round(pais_a * tx_a + pais_a)
    pais_b = round(pais_b * tx_b + pais_b)
    ano = ano + 1

print(f'''
A população do País A de {pais_a} habitantes
ultrapassou o País B de {pais_b} habitantes
após {ano} anos.
''')



