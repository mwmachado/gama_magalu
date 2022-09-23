'''
1. Utilizando a biblioteca numpy siga as instruções abaixo:
    1. Crie um array 6x6 preenchido com zeros
    2. Preencha o centro desse array com um array 4x4 preenchido com uns
    3. Preencha o centro desse array com um array 2x2 preenchido com dois
    4. Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2.
    5. Subtraia o primeiro array pelo segundo
'''

import numpy as np
# [linha, coluna]
array = np.zeros([6,6])
array[1:5, -5:-1] = 1 #np.ones([4,4])
array[2:4, 2:4] = 2 #np.full([2,2], 2)
array2 = np.random.randint(low=0, high=3, size=[6,6])
array3 = array - array2
print(array3)