"""Faça um programa que leia um numero qualquer e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1 = 120"""
n = int(input('Digite o número que quero fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

