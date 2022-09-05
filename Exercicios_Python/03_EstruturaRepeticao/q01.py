# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até (enquanto) que o usuário informe um valor válido.
# enquanto -> while

valido = 'sim'
while valido == 'sim': # condição
    # repetir o código dentro do contexto enquanto a condição for verdadeira
    nota = int(input('Nota: '))
    if 0 <= nota and nota <= 10:
        print('Nota válida!')
        valido = 'sim'
    else:
        print('Nota inválida!')
        valido = 'nao'

print('Fim do programa')

















