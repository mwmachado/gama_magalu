# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
# enquanto -> while

nota = int(input('Nota: '))
if nota >= 0 and nota <= 10:
    print('valor válido')
else:
    while not(nota >= 0 and nota <= 10):
        print('valor inválido')
        nota = int(input('Nota: '))
print('válido')

'''
nota = int(input('Nota: '))
while not(nota >= 0 and nota <= 10):
    print('inválido')
    nota = int(input('Nota: '))

print('válido!')
'''

'''
nota = -1 # valor inválido para começar entrando no loop
while not(nota >= 0 and nota <= 10):
    nota = int(input('Nota: '))
    if nota >= 0 and nota <= 10:
        print('Nota válida!')
    else:
        print('Nota inválida!')
'''