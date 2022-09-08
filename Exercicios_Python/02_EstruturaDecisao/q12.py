'''
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

valor_hora = float(input('Valor Hora: '))
horas_mes = float(input('Horas Mensal: '))
salario = horas_mes*valor_hora
if salario <= 900:
    ir = 0
elif salario <= 1500:
    ir = .05
elif salario <= 2500:
    ir = .1
else:
    ir = .2

print(f'''
============================================
            FOLHA DE PAGAMENTO
============================================

Salário Bruto: (5 * 220)        : R${salario:.2f}
(-) IR (5%)                     : R${salario*ir:.2f}
(-) INSS ( 10%)                 : R${salario*.1:.2f}
FGTS (11%)                      : R${salario*.11:.2f}
Total de descontos              : R${salario*(.1+ir):.2f}
Salário Liquido                 : R${salario*(1-(.1+ir)):.2f}
============================================
''')