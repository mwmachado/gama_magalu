# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Digite o sexo: ')

# match/switch case
# se a letra for m
if letra == 'm' or letra == 'M':
    #if letra.lower() == 'm':
    print('Masculino')
#senão se a letra for f
elif letra.lower() == 'f':
    print('Feminino')
# senão
else:
    print('Sexo inválido!')
    print('O sexo digitado foi', letra)