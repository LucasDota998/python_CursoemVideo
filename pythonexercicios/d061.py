"""Refaça o desafio 51, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while"""
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
termo = t

while c <= 10:
    print('{} '.format(termo),end='')
    termo += r
    c += 1
