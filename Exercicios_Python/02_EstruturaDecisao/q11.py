'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
'''

salario = float(input('Insira o salário: '))

if salario <= 280:
    reajuste = .2
elif salario <= 700:
    reajuste = .15
elif salario <= 1500:
    reajuste = .1
else:
    reajuste = .05

print('Salário antes do reajuste:', salario)
print('Reajuste aplicado: ', reajuste*100, '%', sep='')
print('Aumento aplicado: ', reajuste*salario)
print('Novo salário: ', salario + reajuste*salario)