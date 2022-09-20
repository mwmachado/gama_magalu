'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções:
- uma para fazer a conversão
- uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''
'''
00:00 -> 12 a.m.
12:00 -> 12.p.m.
13:00 -> 1p.m 13-23
'''

def conversao(hora, minuto): #horas:minutos
    if hora == 0:#a.m
        return str(12) + ':' + str(minutos)
    elif hora <= 12 :#1-11 a.m e 12p.m
        return str(hora) + ':' + str(minutos)
    else:#13-23p.m.
        return str(hora-12) + ':' + str(minutos)

def converteTurno(hora):
    if hora >= 12: #12-23
        return 'P'
    else: #0-11
        return 'A'

def saida(turno):
    if turno == 'A': #A
        return 'A.M.'
    else: #P
        return 'P.M.'

opcao = ''
while opcao != 's': # até enquanto a opção for diferente de 's'
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))

    horario = conversao(horas, minutos) #horas:minutos
    turno = converteTurno(horas) # 'A' ou 'P'
    turno = saida(turno) # 'A.M.' ou 'P.M.'

    print(horario + ' ' + turno) #horas:minutos turno
    opcao = input('Continuar - Enter , Sair - s').lower()

print('Fim do Programa!')