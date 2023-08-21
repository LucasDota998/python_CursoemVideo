"""Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha
separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente"""
valores = [[], []]
num = 0
for v in range(1, 8):
    num = (int(input(f'Digite o {v}o valor: ')))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Valores pares em ordem, temos: {valores[0]}')
print(f'Valores impares em ordem, temos: {valores[1]}')