"""Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o tatal de vitórias consecutivas que ele conquistou no final do jogo"""
from random import randint
print('=' * 30)
print(' - JOGO DO PAR OU IMPAR - ')
print('=' * 30)
v = 0

while True:
    jogador = int(input('Digite um número: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR [ P / I ]: ')) .strip() .upper()[0]
    print(f'Vc jogou {jogador} e o computador jogou {pc} e o total deu {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print('GAME OVER')
print(f'Voce teve {v} vitórias consecutivas')


