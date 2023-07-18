"""Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando
o flag (numero de parada)"""
n = 0
escolha = 0
s = 0
while n != 999:
    n = int(input('Digite um valor: '))
    escolha = escolha + 1
    s = s + n
print('Vc escolheu {} números'.format(escolha - 1))
print('A soma entre eles é {}'.format(s - 999))
