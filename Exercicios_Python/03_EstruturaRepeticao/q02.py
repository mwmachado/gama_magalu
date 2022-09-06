'''
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
e voltando a pedir as informações.


while -> validações (repetir até o usuário inserir um valor válido) indefinido
while -> repetição sem final definido
for -> repetição com final definido
'''

nome = input('Usuário: ')
senha = input('Senha: ')
while senha == nome: # condição de repetição
    print('A senha não pode ser igual ao nome do usuário!')
    senha = input('Senha: ')
# caso a condição de execução seja falsa (continua)
# else sem o contexto
print('Informações foram cadastradas com sucesso!')

'''
senha = input('Senha: ')
if senha == nome: # condição de execução
    print('A senha não pode ser igual ao nome do usuário!')
else: # caso a condição de execução seja falsa
    print('Informações foram cadastradas com sucesso!')
'''

# senha será pedida enquanto o usuário digitar um valor inválido (vai ficar preso no loop)
# valor inválido senha == nome
# condição de saída: senha válida -> o usuário só cadastra informações com senha válida