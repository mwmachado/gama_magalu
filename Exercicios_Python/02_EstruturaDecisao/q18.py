# Faça um Programa que peça uma data no formato dd/mm/aaaa e
# determine se a mesma é uma data válida.
# Considerando ano válido entre 1 e 2499 inclusos

data = input('Data (dd/mm/aaaa): ')
partes = data.split('/')

dia = int(partes[0])
mes = int(partes[1])
ano = int(partes[2])

if ano <= 0 or ano >= 2500:
    print('Data Inválida! Ano inválido!')
elif mes < 1 or mes > 12:
    print('Data Inválida! Mês inválido!')
elif dia > 0 and dia < 32:
    if mes == 2 and dia > 29:
        print('Data Inválida! Fevereiro tem no máximo 29 dias!')
    elif mes in (4,6,9,11) and dia > 30:
        print('Data Inválida! Esse mês tem no máximo 30 dias!')
    else:
        print('Data Válida!')
else:
    print('Data Inválida! Dia inválido')