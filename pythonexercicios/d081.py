"""Crie um programa qua vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
A - Quantos números foram digitados.
B - A lista de valores de forma decrescente
C - Se o valor 5 foi digitado e está ou não na lista"""
valores = list()
total = 0

while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    total += 1
    r = str(input('Deseja continuar[S/N]: ')).upper()
    if r == 'S':
        continue
    else:
        break
print(f'Foram digitados {total} valores')
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram: {valores}')
if 5 in valores:
    print('O número 5 FOI digitado na lista')
else:
    print('O número 5 NÃO está na lista!')
