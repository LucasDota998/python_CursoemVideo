"""Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha
separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente"""
valores = list()
for v in range(1,8):
    valores.append(int(input(f'Digite o {v}o valor: ')))
print(valores)
