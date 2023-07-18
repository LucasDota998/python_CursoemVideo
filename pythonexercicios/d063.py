"""Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequencia de fibonacci.
ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 - ..."""
print('=' * 28)
print('- Sequencia de Fibonaci -')
print('=' * 28)
n = int(input('Deseja ver quantos termos da sequencia? '))
t1 = 0
t2 = 1
c = 3
print(' {} {} '.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print(' {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
