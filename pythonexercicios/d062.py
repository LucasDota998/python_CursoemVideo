"""Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa vai parar quando ele disser que quer mostrar 0 termos"""

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = t
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos: '))
print('Progressão finalizada!')
    