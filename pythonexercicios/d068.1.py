"""Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o tatal de vitórias consecutivas que ele conquistou no final do jogo"""
from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR [P/I]:')).strip() .upper()
    print(f'Voce digitou {jogador} e o computador digitou {pc}. A soma deu {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Vc VENCEU!')
            v += 1
        else:
            print('Vc PERDEU')
            break
    print('Vamos jogar novamente...')
print('GAME OVER!!')
print(f'Voce venceu {v} vezes consecutivas')