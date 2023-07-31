"""Programa de banco com saque e deposito mostrando o saldo final"""
total = 0
banco = ' '
while True:
    desejo = str(input('Deseja fazer operação [S/N] :')).upper()
    if desejo == 'S':
        banco = str(input('Deseja sacar ou depositar [S/D]: ')).upper()
        if banco == 'D':
            deposito = float(input('Qual o valor a ser depositado: '))
            total += deposito
        if banco == 'S':
            saque = float(input('Qaual valor será sacado: '))
            total -= saque
    else:
        print('Programa finalizado')
        break
print(f'Seu saldo final é de {total} reais ')