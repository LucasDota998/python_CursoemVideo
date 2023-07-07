# Facça um programa que leia tres números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceito número: '))
# verificando o menor
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('Dentre so números escolhidos, o {} é o MAIOR, e o {} é o MENOR'.format(maior, menor))
