"""Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A - Quantas pessoas foram cadastradas
B - Uma listagem com as pessoas mais pesadas
C - Uma listagem com as pessoas mais leves"""
totalpessoas = 0
pessoas = list()

pesados = list()
leves = list()

while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    if peso > 100:
        pesados.append(nome)
    else:
        leves.append(nome)
    resp = str(input('Deseja continuar[S/N]: '))
    totalpessoas += 1
    if resp in 'Nn':
        break
print(f'Foram cadastradas {totalpessoas} pessoas')
print(f'Pessoas leves (abaixo de 100 kg): {leves}')
print(f'Pessoas pesadas (acima de 100 kg): {pesados}')