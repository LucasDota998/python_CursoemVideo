"""Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:

-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes"""


l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Isso pode ser um triangulo')
    if l1 == l2 == l3:
        print('Esse triangulo é EQUILATERO')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('Isso é um traingulo ISÓSCELES')
    else:
        print('Isso é um triangulo ESCALENO')
else:
    print('Não pode ser um triangulo')
