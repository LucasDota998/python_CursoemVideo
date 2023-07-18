"""Faça um programa que calcule a soma entre todos os numeros ìmpares que são multiplos de tres e se encontram
entre 1 até 500"""
c = 1
soma = 0
while c < 500:
    c += 1
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
print('A soma entre os número impares e multiplos de 3 é {}'.format(soma))
