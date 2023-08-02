"""Crie um programa que vai gerar cinsco números aleatórios e colocar em um tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla"""
from random import randint
maior = menor = cont = 0
sort = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
print(f'Os valores sorteados foram: {sort}')
print(f'O maior valor sorteado foi: {max(sort)}')
print(f'O menor valor sorteado foi: {min(sort)}')
