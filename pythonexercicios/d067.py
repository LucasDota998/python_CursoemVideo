"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo"""
c = 0

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(0, 11):
        produto = (n * c)
        print(f'{n} x {c} = {produto}')
        c += 1

print('Programa encerrado!')



