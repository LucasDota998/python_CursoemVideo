#Facça um programa que leia tres números e mostre qual é o maior e qual é o menor.
pri = int(input('Digite o primeiro número: '))
sec = int(input('Digite o segundo número: '))
ter = int(input('Digite o terceito número: '))
if pri > sec > ter:
    print('O maior valor é: {}'.format(pri))
if sec > pri > ter:
    print('o maior valor é {}'.format(sec))
if ter > sec > pri:
    print('O maior valor é: {}'.format(ter)?)