'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre zero e 4.0        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2

if media <= 4:
    conceito = 'E'
    situacao = 'Reprovado'
elif media <= 6:
    conceito = 'D'
    situacao = 'Reprovado'
elif media <= 7.5:
    conceito = 'C'
    situacao = 'Aprovado'
elif media <= 9:
    conceito = 'B'
    situacao = 'Aprovado'
else:
    conceito = 'A'
    situacao = 'Aprovado'

print(f'''
============
Notas
============

Nota 1  : {str(n1):>10}
Nota 2  : {str(n2):>10}
Média   : {str(media):>10}
Conceito: {conceito:>10}
Situação: {situacao:>10}
''')