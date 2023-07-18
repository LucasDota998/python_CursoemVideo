"""Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valar lido. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores"""
r = 'S'
media = 0
soma = 0
total = 0
maior = 0
menor = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [ S / N ] ')).upper()
    total = total + 1
    soma = soma + n
    media = soma / total
    if total == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print('A soma entre os valores é de: {}'.format(soma))
print('A média entre eles é: {:.2f}'.format(media))
print('O maior valor foi: {}'.format(maior))
print('O menor valor foi: {}'.format(menor))
print('Programa finalizado!')
