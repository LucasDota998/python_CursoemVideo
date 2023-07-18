"""Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 1 a 10. Só que agora o jogador vai
tentar adivinhas até acertar, mostrando no final quantos palpites foram necessários para vencer """
from random import randint
escolhido = randint(0, 10)
print('Vou pensar num número entre 0 e 10. Tente acertar...')
palpites = 0
tentativa = 0
while tentativa != escolhido:
    tentativa = int(input('Qual o seu palpite: '))
    palpites += 1

print('Vc ACERTOU. Eu pensei no número {} e vc usou {} tentativas'.format(escolhido, palpites))


