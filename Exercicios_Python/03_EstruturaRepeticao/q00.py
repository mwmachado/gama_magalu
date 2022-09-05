saldo = 100.00
saque = 0
while saldo > 0:
    saque = float(input('Quando deseja sacar:'))
    if saque <= saldo:
        saldo = saldo - saque
        # saldo -= saque ==> saldo = saldo - saque
        # saldo += saque ==> saldo = saldo + saque
        # saldo *= saque ==> saldo = saldo * saque
        # ...
        print(f'Você sacou R${saque:.2f}!')
        print(f'Seu saldo é de R${saldo:.2f}')
    else:
        print('Você não tem saldo suficiente para essa operação!')

print('Fim do programa!')