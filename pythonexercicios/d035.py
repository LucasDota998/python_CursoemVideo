# Crie um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar
#um triangulo
l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Isso pode ser um triangulo')
else:
    print('Não pode ser um triangulo')
