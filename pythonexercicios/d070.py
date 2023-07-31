"""Crie um programa que leia o nome e o preço de vários produtos. Oprograma deverá perguntar se o usuário vai continuar.
No final, mostre:
A - Qual é o total gasto na conta
B - Quantos produtos custam mais de 1000 reias
C - Qual é o nome do produto mais barato"""
print('=' * 25)
print('  CADASTRO DE PRODUTOS')
print('=' * 25)
total = m1000 = menor = barato = cont = 0
while True:
    add = str(input('Deseja adicionar algum produto [S/N]: ')) .upper()
    if add == 'S':
        nome = str(input('Qual o nome do produto: '))
        preco = float(input('Qual o preço do produto: '))
        total = total + preco
        cont += 1
        if preco > 1000:
            m1000 += 1
        if cont == 1 or preco < menor:
            menor = preco
            barato = nome
    else:
        print('Programa finalizado com sucesso!')
        break
print(f'O total gasto na loja foi de {total:.2f}')
print(f'Acima de 1000 reais temos {m1000} produtos')
print(f'O produto mais barato foi {barato}')