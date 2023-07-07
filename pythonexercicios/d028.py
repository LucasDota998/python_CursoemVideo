#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual o foi o número escolhido pelo computador
#O programa deverá escreve na tela se o usuário venceu ou perdeu
import random
from time import sleep
tentativa = int(input('Escolha um número: '))
lista = [1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print('PROCESSANDO...')
sleep(2)

if tentativa == escolhido:
    print('VOCE ACERTOU!!!')
else:
    print('VC ERROU!!!')

print('O número escolhido foi: {}'.format(escolhido))
