n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
n4 = int(input('N4: '))
n5 = int(input('N5: '))

maior = 0
for n in n1, n2, n3, n4 ,n5:
    if maior > n:
        maior = maior
    else:
        maior = n

print('O maior número entre eles é ', maior)

'''
maior = 0
while contador<=5:
    n = int(input("Digite um numero: "))
    if(n > maior):
        maior = n
    contador=contador+1
print("o maior numero digitado foi:",maior)
'''