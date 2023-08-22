"""Aprimore o ex 86 mostrando:
A  - A soma de todos os valores pares
B - A soma dos valores da terceira coluna
C - O maior valor da segunda linha"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = mai = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l},{c}]: '))
print('=' * 30)
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if l >= 0 and c == 2:
            soma3 += matriz[l][c]
    print()
for c in range (0,3):
     if c == 0:
         mai = matriz[1][c]
     elif matriz[1][c] > mai:
         mai = matriz[1][c]




print('=' * 30)
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma das terceira coluna é: {soma3} ')
print(f'O maior valor da segunda linha é: {mai}')