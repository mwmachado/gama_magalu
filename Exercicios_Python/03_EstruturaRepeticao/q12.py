'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
'''

print('''
=============
   Tabuada
=============
''')

##

# condição de entrada do loop = número inválido, numero < 0 or numero < 10
# condição de saída do loop = número válido , numero >= 0 or numero <= 10
# condição de entrada do loop = número não válido = not(numero >= 0 or numero <= 10)

# numero = -1
# enquanto o usuário não digitar um número entre 0 e 10

#numero = -1
# Garantir que o usuário vai inserir um valor válido antes de calcular a tabuada
numero = int(input('Número: ')) #-1,-2,-3,... ou 11,12,13,14
while numero < 0 or numero > 10: # condição loop
    print('Número inválido, digite um valor entre 0 e 10')
    numero = int(input('Numero: '))

## Agora que temos um número válido vamos calcular a tabuada
print('Calculando a tabuada...')

'''
fator = 0 #contador
while fator <= 10:
    print(f'{fator} X {numero} = {numero*fator}')
    fator = fator + 1
    #fator +=1
'''

# para variável em uma lista de opções, repita o código
for fator in 0,1,2,3,4,5,6,7,8,9,10:
    print(f'{fator} X {numero} = {numero*fator}')

print('Fim do programa!')
