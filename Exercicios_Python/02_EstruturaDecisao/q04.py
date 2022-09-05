# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    print('vogal')
else:
    print('consoante')
'''
'''
- digita um valor inválido [1,2,%,-, ..]
- digita uma consoante [b,c,d,e,f,..]
- digita uma vogal [a,e,i,o,u]
'''
letra = input('Digite uma letra: ')
# se a letra não está no alfabeto
if not letra.isalpha():
    print('Valor inválido!')
# in/inside -> dentro
# se a letra está dentro de 'aeiou'
elif letra.lower() in 'aeiou':
    print('vogal')
# se for consoante
else:
    print('consoante')
