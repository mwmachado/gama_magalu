'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres; # no mínimo 4
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Nome: ')
while not (len(nome) > 3): # condição de repetição nome não-válido
#while len(nome) <= 3:
    print('Nome inválido! O nome deve conter mais de 3 caracteres.')
    nome = input('Nome: ')
# condição de saída nome válido
print('Nome válido!')

idade = int(input('Idade: '))
while idade < 0 or idade > 150: #condição de repetição idade inválida
#while not(idade >= 0 or idade <= 150): 
    print('Idade inválida! A idade deve estar entre 0 e 150.')
    idade = int(input('Idade: '))
# condição de saída idade válida
print('Idade válida!')

salario = float(input('Salário: '))
while salario <= 0:
    print('Salário inválido! O salário tem que ser maior que 0.')
    salario = float(input('Salário: '))
print('Salário válido!')

genero = input('Sexo (f ou m): ') #.lower()
while genero != 'f' and genero != 'm':
#while not(genero == 'f' or genero == 'm')
    print("Gênero inválido! letras permitidas 'f', 'm'")
    genero = input('Sexo (f ou m): ')
print('Gênero válido!')

estado = input('Estado civil (s, c, v, ou d): ') #.lower()
while estado not in 'scvd':
    print("Estado Civil inválido! letras permitidas 's', 'c', 'v', 'd'")
    estado = input('Estado civil (s, c, v, ou d): ')
print('Estado Civil válido!')