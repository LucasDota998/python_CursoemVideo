"""Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa vai parar quando ele disser que quer mostrar 0 termos"""

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
escolha = 0
c = 1
termo = t

while c <= 10:
    print('{} '.format(termo),end='')
    termo += r
    c += 1
    print('Deseja mostrar mais quantos termos: ')
    