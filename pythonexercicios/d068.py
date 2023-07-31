"""Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o tatal de vitórias consecutivas que ele conquistou no final do jogo"""
from random import randint
print('=' * 30)
print(' - JOGO DO PAR OU IMPAR - ')
print('=' * 30)

escolha = str(input('PAR ou IMPAR[ P / I ]: ')) .upper() .strip()
n = int(input('Digite um número: '))
pc = randint(1, 10)
print(pc)
