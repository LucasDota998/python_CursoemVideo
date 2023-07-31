"""Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a
soma entre eles, desconsiderando o flag"""
soma = 0
total = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    total = total + 1
    soma += n
print(f'A soma dos valores é {soma} e foram ditados {total} números.')