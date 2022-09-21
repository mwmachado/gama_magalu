'''
Jogo de Craps.
Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

from random import randint
def craps():
    rodada = 1
    resultado = ''
    ponto = 0
    while not (resultado == 'ganhou' or resultado == 'perdeu'):
        dados = randint(2, 12)
        print(f'Dados mostrado pelo computador = {dados}')
        if rodada == 1 and dados in (7, 11):
            print('Natural')
            print('GANHOU!')
            resultado = 'ganhou'
        elif rodada == 1 and dados in (2, 3, 12):
            print('CRAPS')
            print('Você perdeu')
            resultado = 'perdeu'
        elif rodada == 1 and dados in (4, 5, 6, 8, 9, 10):
            print('Ponto')
            ponto = dados
        else:
            if dados == 7:
                print('Você perdeu!')
                resultado = 'perdeu'
            elif dados == ponto:
                print('Você ganhou!')
                resultado = 'ganhou'
        rodada = rodada + 1
        input('Enter')
    print('Fim do jogo!')
craps()