''' Diferença entre escrever e retornar
def escreve_10():
    #volta para linha 1 e executa tudo que estiver dentro do contexto
    print(10)

def retorna_10():
    #volta para linha 5 e executa tudo que estiver dentro do contexto
    return 10 # encerra a função retornado o valor 10

var = escreve_10()
print(var)

var = retorna_10()
print(var)
'''

'''
# não recomendado
def soma_sem_parametro():
    n1 = int(input('N1:'))
    n2 = int(input('N2:'))
    return n1+n2

print(soma_sem_parametro())

# boa prática
def soma_com_parametro(parametro1, parametro2):
    #parametro1 = n2
    #parametro2 = n1
    return parametro1+parametro2

n1 = int(input('N1:'))
n2 = int(input('N2:'))
print(soma_com_parametro(n2, n1))
'''

''' return indica o final da função 
def escreve_retorna_10(n1):
    #n1 = 10
    if n1 > 0:
        print(n1) # retorna n1 e encerra a função
    
    print(f'{n1} número inválido!')

var = escreve_retorna_10(10)
print(var)

var = escreve_retorna_10(-1) #None
print(var)
'''

'''
#global
def circunferencia(raio):
    print(2*pi*raio)

def area_circulo(raio):
    print(pi*raio**2)

x = 10 #global
pi = 3.14 #global
circunferencia(x)
area_circulo(x)
'''
'''
#local
def circunferencia(raio):
    # raio = x
    pi = 3.14 #local
    raio = 5 #não afeta o valor de x, pq a função só pega o valor da variável x e não o objeto em si
    print(2*pi*raio)

def area_circulo(raio2):
    # pi = 3.14 #local
    print(pi*raio2**2)

x = 10 #global
circunferencia(x)
area_circulo(x)

# exemplo2
global1 = 10
global2 = 15
def soma(local1,local2):
    # local1 = 15
    # local2 = 10

    print(local1+local2)
    return local1 + local2 #15 #25
    # as variáveis são limpadas da memória

resultado = soma(global2,global1) # volta para linha 91 e executa todo o contexto
# print(local1) # não executa pq o python limpa as variáveis ao final da execução da função
'''

''' Estruturas de dados são exceção a regra, e portanto, as variáveis globais são alteradas dentro das funções
catalogo = []
copia_catalogo = catalogo.copy()
def adiciona_item_catalago(catalogo_local, item):
    # catalogo_local = []
    catalogo_local.append(item)
    # apaga o catalogo local

adiciona_item_catalago(catalogo, 'arroz')
adiciona_item_catalago(catalogo, 'feijão')
adiciona_item_catalago(catalogo, 'carne')
print(catalogo) #catalogo vazio
print(copia_catalogo)
'''
'''
# Parametros opcionais

def ola(nome='mundo'):
    # se o parâmetro nome não for definido, utiliza-se mundo
    #nome = 'matheus' #local
    print(f'Olá! {nome}!')
    # apaga a variável nome

ola('matheus')
ola('bruno')
ola('gabrielle')
ola()
#print(nome)

def soma(n1=0, n2=0):
    print(n1+n2)
    return n1+n2

soma(10, 20)
soma(10)
soma()
'''
'''
def pedir_acai(gramas, opcionais=''):                                        
    if len(opcionais) > 0:
        print(f'Entregando açaí de {gramas}g com os opcionais {opcionais}!')
    else:
        print(f'Entregando açaí de {gramas}g')

pedir_acai(300)
pedir_acai(500, 'mel')
pedir_acai(opcionais=0, gramas=700)

'''
'''
# Ordem dos parâmetros
def area(lado=0, raio=0, pi=3.14, base=0, altura=0):
    if lado > 0:
        print(f'a area do quadrado é {lado**2}')
    elif raio > 0:
        print(f'a area do circulo é {pi*raio**2}')
    elif base > 0 or altura > 0:
        print(f'a area do triângulo é {base*altura/2}')
    else:
        print('nada a calcular')

area(10)
area(lado=10)
area(raio=4)
area(0, 4)
area(altura=2,base=5)
area(0,0,3.14,5,2)
area(lado=10, raio=4)
area()
'''
'''Alterando valor de variáveis globais dentro da função
ganhando=''
x = 10 #global
def soma_5(numero):
    #global x #para alterar o valor da variável na linha de cima
    x = 15 #local
    print(x) # o python dá preferencia pela variável local
    #numero = 10
    numero = numero + 5 #local
    print(numero)
    # apaga a varial local numero

soma_5(x)
print(x)
'''
'''
x = [10,15] #global
def soma_5(lista):
    # global x
    # lista = x
    # lista[0] = lista[0]+5
    # lista = [15,20]
    
    # lista[0] = lista[0] + 5
    # lista[1] = lista[1] + 5
    for numero in range(len(lista)):
        lista[numero] = lista[numero] + 5
    
    print(lista)

soma_5(x)
print(x)
'''