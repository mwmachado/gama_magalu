'''
3. Crie um array com três dimensões, onde a primeira dimensão são os dias da semana (seg a dom), a segunda dimensão são as semanas do mês (considere apenas 4 para todos os meses), e a terceira são os meses do ano (Jan a dezembro).
  1. Marque os finais de semana com a letra W
  2. Marque o começo do mês com a letra S
  3. Marque o final do mês com a letra E
  4. Marque os demais dias com a letra D
  5. Marque os feriados nacionais com a letra F
    - 01/01 - Ano novo
    - 15/04 - Paixão de Cristo
    - 21/04 - Tiradentes
    - 01/05 - Dia do Trabalho
    - 07/09 - Independência do Brasil
    - 12/10 - Nossa Senhora Aparecida
    - 02/11 - Finados
    - 15/11 - Proclamação da República
    - 25/12 - Natal
'''

# %% Criação do calendário
import numpy as np
#[mes, semana, dia]
# 4 semanas * 7 dias = 28 1-28
dias = np.arange(start=1, stop=29, dtype=object)#.reshape([1, 4, 7]) #str->object
mes = dias.reshape([1, 4, 7])
calendario = np.repeat(mes, 12, axis=0)
calendario

# %% Marcação dos finais de semana
#[mes, semana, dia]
calendario[:, :, [0, -1]] = 'W'
calendario

# %% Marcação do primeiro dia do mês
#[mes, semana, dia]
calendario[:, 0, 0] = 'S'
calendario

# %% Marcação do último dia do mês
#[mes, semana, dia]
calendario[:, -1, -1] = 'E'
calendario

# %% Marcação dos demais dias
#~np.isin(calendario, ['W', 'S', 'E'])
#[mes, semana, dia]
calendario[:, :, 1:-1] = 'D'
calendario

# %% Marcação dos feriados
# [mes, semana, dia]
mes    = [0, 3, 3, 4, 8, 9, 10, 10, 11]
semana = [0, 2, 2, 0, 0, 1, 0, 2, -1]
dia    = [0, 0, -1, 0, -1, 4, 1, 0, 3] 
calendario[mes, semana, dia] = 'F'
calendario

print(calendario) 