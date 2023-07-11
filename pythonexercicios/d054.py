"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores"""
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Em que ano vc nasceu: '))
    if atual - ano >= 18:
        maior = maior + 1

    else:
        menor = menor + 1
print('Com a maioridade temos {} pessoas, e ainda menores temos {} pessoas'.format(maior, menor))
