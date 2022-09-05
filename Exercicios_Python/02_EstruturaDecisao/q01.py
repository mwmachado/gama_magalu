#Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('N1:')) #10
n2 = float(input('N2:')) #20

#print('O maior número é', max(n1, n2))

if n1 > n2: # condição n1 ser maior que n2
    # True
    print('O maior número é', n1)
# senão, vai ser executado caso a condição seja Falsa
else:
    # False
    print('O maior número é', n2)

print('Fim do programa!')