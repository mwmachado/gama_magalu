'''
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
import math

arquivo = float(input('Tamanho do arquivo (MB):'))
velocidade = float(input('Velocidade do link de Internet (Mbps): '))
velocidade_MBs = velocidade/8
segundos = arquivo/velocidade_MBs

print('Tempo aproximado de download: ', segundos//60, 'min', math.ceil(segundos%60), 's')