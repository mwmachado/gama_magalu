'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input('Digite o turno: ')
if turno.upper() == 'M':
    print('Bom Dia!')
elif turno.upper() == 'V':
    print('Bom Tarde!')
elif turno.upper() == 'N':
    print('Bom Noite!')
else:
    print('Valor inválido!')
