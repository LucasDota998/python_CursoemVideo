"""Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher"""
n = int(input('Digite um número: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, (n*c)))
