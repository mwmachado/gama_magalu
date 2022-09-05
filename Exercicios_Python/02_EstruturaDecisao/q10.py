'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input('Digite o turno: ').upper()
#turno = turno.upper()

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
#elif turno.lower() == 'v':
    print('Bom Tarde!')
elif turno == 'N':
    print('Bom Noite!')
else:
    print('Valor inválido!')
