"""Faça um programa que leia 5 valores numericos e guarde-os em um lista.
No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista"""
valores = list()
maior = menor = 0

for v in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]


print(f'Voce digitou os segintes valores: {valores}')
print(f'O maior valor é {maior} e está na posição', end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f' {i} ', end='')
print()
print(f'O menor valor é {menor} e está na posição', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i} ', end='')
print()








