# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('N1:'))
n2 = float(input('N2:'))
n3 = float(input('N3:'))


#print('O maior número é', max(n1, n2, n3))
#print('O menor número é', min(n1, n2, n3))

print('o maior número é', end=' ')
if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

print('o menor número é', end=' ')
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)