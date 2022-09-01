'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
print('==============================')
print('CALCULADORA DE SALÁRIO LÍQUIDO')
print('==============================')

valor_hora = float(input('Quanto você ganha por hora? '))
hora_trabalhada = int(input('Quanta horas trabalhadas no mês? '))
s_bruto = valor_hora*hora_trabalhada
descontos = s_bruto*(.11 + .08 + .05)

print()
print('+ Salário Bruto : R$', s_bruto)
print('- IR (11%) : R$', s_bruto*.11)
print('- INSS (8%) : R$', s_bruto*.08)
print('- Sindicato ( 5%) : R$', s_bruto*0.05)
print('= Salário Liquido : R$', s_bruto-descontos)
print('==============================')