'''
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; [7,...]
A mensagem "Reprovado", se a média for menor do que sete; [1,2,...,6.9]
A mensagem "Aprovado com Distinção", se a média for igual a dez. [10]
'''

media = float(input('Digite o valor: '))
if media >= 7: # and media != 10
    if media == 10:
        print('Aprovado com Distinção!')
    else:
        print('Aprovado!')
else:
    print('Reprovado!')

