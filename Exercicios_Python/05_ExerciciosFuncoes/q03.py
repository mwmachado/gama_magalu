#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def questao03(n1,n2,n3):
    soma = n1+n2+n3 #local
    print(f'A soma é {soma}!') #imprimir
    return soma #retornar
    #ao final da execucao a função apaga a variável soma

n1=int(input('N1: '))
n2=int(input('N2: '))
n3=int(input('N3: '))

resultado = questao03(n1,n2,n3) #None
#print(f'A soma é {questao03(n1,n2,n3)}!')
#resultado = 6
print(resultado)