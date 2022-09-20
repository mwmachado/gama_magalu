'''
To Do (Tarefas a fazer)
- [] No menu de cadastro ao pedir o valor do produto já colocar o nome do produto
- [] Explicar para o usuário o que está errado quando insere valor com ','.
- [] Adicionar uma função de limpar tela que funcione em windows e linux.
- [] Melhorar os relatórios
'''

#Setup
import os


#Funções
def menu(menu):
    os.system('clear')
    print(menu)

def cadastrar_produtos(produtos):
    chave = input('Nome do produto: ')
    while len(chave) == 0:
        print('Valor inválido!')
        chave = input('Nome do produto: ')

    valor = input('Valor do produto: ')
    while not valor.replace('.', '', 1).isdigit(): #.replace(',', '.')
        print('Valor inválido!')
        valor = input('Valor do produto: ')
    
    produtos[chave] = valor
    print('Produto Cadastrado!')

# Boas Vindas
boas_vindas = '''
==========================
Bem vindo(a) ao Organico's
==========================
'''

# Menu
principal = '''
=======================
       Navegação
1. Cadastro
2. Vendas
3. Relatório
0. Sair
=======================
'''
opcoes_menu = '0123'

# Cadastro
menu_cadastro = '''
=======================
       Cadastro
1. Cadastrar Produto
2. Listar Produto
3. Deletar Produto
0. Sair
=======================
'''
opcoes_cadastro = '0123'
produtos = {} #{produto: valor}

# Vendas
menu_vendas = '''
========================
       Vendas
1. Adicionar ao carrinho
2. Mostrar o carrinho
3. Remover do carrinho
4. Finalizar venda
0. Sair
========================
'''
opcoes_vendas = '01234'
carrinho = {} #{produto: quantidade}

# Relatório
menu_relatorio = '''
========================
       Relatório
1. Quantidade vendida
2. Vendas por produto
3. Vendas Total
0. Sair
========================
'''
opcoes_relatorio = '0123'
relatorio = [] # [{produto: quantidade},...]

# Tela de Boas-vindas
menu(boas_vindas)
input('Aperte Enter para Continuar')

# Menu de Navegação
opcao = 1 # inicializando a variável para entrar no loop
while opcao != '0':
    menu(principal)
    opcao = input('Opção: ')
    if opcao not in opcoes_menu:
        print('Opção inválida!')
        input('Aperte Enter para Continuar')
    else:
        # Menu Cadastro
        if opcao == '1':
            while opcao != '0':
                menu(menu_cadastro)
                opcao = input('Opção: ')
                if opcao not in opcoes_menu:
                    print('Opção inválida!')
                else:
                    if opcao == '1':
                        cadastrar_produtos(produtos)
                    elif opcao == '2': # listar produtos
                        print()
                        print(f'|{"Produto":10s}|{"Preço":>10s}|')
                        print('|'+'-'*10+'|'+'-'*10+'|')
                        for chave, valor in produtos.items():
                            print(f'|{chave:10s}|{valor:>10s}|')
                        print('-' * 23)
                    elif opcao == '3': # deletar produtos
                        if len(produtos) > 0: #if produto:
                            for chave in produtos:
                                print(chave)
                            
                            chave = input('Qual produto deseja deletar? ')
                            while chave not in produtos:
                                print('Produto não encontrado.')
                                chave = input('Qual produto deseja deletar? ')
                            
                            del produtos[chave] #produtos.pop(chave)
                            print('Produto deletado!')
                        else:
                            print('Não há produtos')
                    else:
                        print('Saindo do menu de Cadastro')
                input('Aperte Enter para Continuar:')
            opcao = 1 # resetar variável opcao
        elif opcao == '2':
            while opcao != '0':
                menu(menu_vendas)
                opcao = input('Opção: ')
                if opcao not in opcoes_vendas:
                    print('Opção inválida!')
                else:
                    if opcao == '1': # Adicionar ao carrinho
                        if len(produtos) > 0:
                            print()
                            print(f'|{"Produto":10s}|{"Preço":>10s}|')
                            print('|'+'-'*10+'|'+'-'*10+'|')
                            for chave, valor in produtos.items():
                                print(f'|{chave:10s}|{valor:>10s}|')
                            print('-' * 23)
                            
                            chave = input('Qual produto deseja adicionar? ')
                            while chave not in produtos:
                                print('Produto não encontrado')
                                chave = input('Qual produto deseja adicionar? ')
                            
                            qtd = input('Quantas unidades? ')
                            while not qtd.replace('.', '', 1).isdigit():
                                print('Quantidade inválida!')
                                qtd = input('Quantas unidades? ')
                            
                            if chave in carrinho:
                                carrinho[chave] = float(carrinho[chave]) + float(qtd)
                                carrinho[chave] = str(carrinho[chave])
                            else:
                                carrinho[chave] = qtd
                            
                            print(f'Adicionado {qtd} unidade(s) do produto {chave} ao carrinho.')
                        else:
                            print('Não há produtos cadastrados!')
                    elif opcao == '2': # Mostrar o carrinho
                        print()
                        print(f'|{"Carrinho":10s}|{"Quantidade":>10s}|')
                        print('|'+'-'*10+'|'+'-'*10+'|')
                        for chave, valor in carrinho.items():
                            print(f'|{chave:10s}|{valor:>10s}|')
                        print('-' * 23)
                    elif opcao == '3': # Remover do carrinho
                        if len(carrinho) > 0:
                            print()
                            print(f'|{"Carrinho":10s}|{"Quantidade":>10s}|')
                            print('|'+'-'*10+'|'+'-'*10+'|')
                            for chave, valor in carrinho.items():
                                print(f'|{chave:10s}|{valor:>10s}|')
                            
                            chave = input('Qual item deseja remover? ')
                            while chave not in carrinho:
                                print('Este item não está no carrinho!')
                                chave = input('Qual item deseja remover? ')
                            
                            del carrinho[chave]
                            print(f'Item {chave} removido do carrinho!')
                        else:
                            print('Carrinho vazio!')
                    elif opcao == '4': # Finalizar venda
                        if len(carrinho) > 0:
                            print()
                            print(f'|{"Carrinho":10s}|{"Quantidade":>10s}|{"Preço":>10s}|')
                            print('|'+'-'*10+'|'+'-'*10+'|'+'-'*10+'|')

                            total = 0
                            for chave, quantidade in carrinho.items():
                                preco = float(quantidade) * float(produtos[chave])
                                total = total + preco #total += preco
                                print(f'|{chave:10s}|{quantidade:>10s}|{str(preco):>10s}|')
                            
                            print('-'*34)
                            print(f'Total: R${total}')
                            
                            relatorio.append(carrinho.copy())
                            print('Venda registrada na aba de Relatórios!')
                            carrinho.clear()
                            print('Carrinho finalizado!')
                        else:
                            print('Carrinho vazio!')
                    else:
                        print('Saindo do menu de Vendas')
                input('Aperte Enter para Continuar:')

            opcao = 1 # resetar variável opcao
        elif opcao == '3':
            while opcao != '0':
                menu(menu_relatorio)
                opcao = input('Opção: ')
                if opcao not in opcoes_menu:
                    print('Opção inválida!')
                else:
                    #setup
                    consolidado={}
                    for venda in relatorio:
                        for chave in venda:
                            if chave in consolidado:
                                consolidado[chave] = str(float(consolidado[chave]) + float(venda[chave]))
                            else:
                                consolidado[chave] = venda[chave]

                    if opcao == '1': # Quantidade por produto
                        if len(relatorio)>0:
                            print()
                            print(f'|{"Produto":10s}|{"Quantidade":>10s}|')
                            print('|'+'-'*10+'|'+'-'*10+'|')
                            for chave, valor in consolidado.items():
                                print(f'|{chave:10s}|{valor:>10s}|')
                            print('-' * 23)
                        else:
                            print('Nenhuma venda foi realizada ainda!')
                    elif opcao == '2': # Vendas por produto
                        if len(relatorio)>0:
                            print()
                            print(f'|{"Produto":10s}|{"Total (R$)":>10s}|')
                            print('|'+'-'*10+'|'+'-'*10+'|')
                            for chave, quantidade in consolidado.items():
                                preco = str(float(quantidade) * float(produtos[chave]))
                                print(f'|{chave:10s}|{preco:>10s}|')
                            
                            print('-'*23)
                        else:
                            print('Nenhuma venda foi realizada ainda!')
                    elif opcao == '3': # Vendas Total
                        if len(relatorio)>0:
                            print()
                            print(f'|{"Produto":10s}|{"Quantidade":>10s}|{"Preço":>10s}|')
                            print('|'+'-'*10+'|'+'-'*10+'|'+'-'*10+'|')

                            total = 0
                            for chave, quantidade in consolidado.items():
                                preco = float(quantidade) * float(produtos[chave])
                                total = total + preco
                                print(f'|{chave:10s}|{quantidade:>10s}|{str(preco):>10s}|')
                            
                            print('-'*34)
                            print(f'Total: R${total}')
                        else:
                            print('Nenhuma venda foi realizada ainda!')
                input('Aperte Enter para Continuar:')
            opcao = 1 # resetar variável opcao
        else:
            print('Obrigado e Volte Sempre!')
