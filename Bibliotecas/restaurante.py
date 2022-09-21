#import receitas
#from receitas import fritar_ovo, fazer_miojo
from receitas import *
#import receitas.brasileiras
from receitas.brasileiras import feijoada
#import receitas.asiaticas
from receitas.asiaticas import pedir_sushi
#import receitas.italianas
from receitas.italianas import carbonara

'''
def carbonara():
    print('carbonara mais simples')


receitas.italianas.carbonara()
carbonara()
'''

menu = '''
1. ovo
2. miojo
3. feijoada
4. sushi
5. carbonara
'''
print(menu)
opcao = int(input('Qual prato voce quer? '))

if opcao == 1:
    #receitas.fritar_ovo()
    fritar_ovo()
elif opcao == 2:
    #receitas.fazer_miojo()
    fazer_miojo()
elif opcao == 3:
    #receitas.brasileiras.feijoada()
    feijoada()
elif opcao == 4:
    #receitas.asiaticas.pedir_sushi()
    pedir_sushi()
else:
    #receitas.italianas.carbonara('ovo', 'bacon', 'queijo', 'macarrao')
    carbonara('ovo', 'bacon', 'queijo', 'miojo')