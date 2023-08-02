"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla. No final, mostre:
A - Quantas vezes o número 9 apareceu
B - Em que posição foi digitado o primeiro valor 3.
C - quais foram os número pares"""
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
numeros = (n1, n2, n3, n4)
print(f'Os valores digitados foram: {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 está na posição: {numeros.index(3)+1}')
else:
    print('O valor três não foi digitado')
for n in numeros:
    if n % 2 == 0:
        print(f' Os valor pares foram: {n}')
