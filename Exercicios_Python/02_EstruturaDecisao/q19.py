'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e",
da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

numero = int(input('Número: '))
if numero > 0 and numero < 1e3:
    centenas = numero//100
    dezenas  = numero%100//10
    unidades = numero%100%10
    if centenas:
        print(f"{centenas} {'centena' if centenas == 1 else 'centenas'}", end='')
    if dezenas:
        print(', ' if unidades else ' e ', end='')
        print(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}", end='')
    if unidades:
        print(' e ', end='')
        print(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}")
    print()
else:
    print('O número deve ser inteiro e menor que 1000!')
print()