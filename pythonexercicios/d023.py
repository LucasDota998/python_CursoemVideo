#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex: 1834 = unidades:4 / dezenas:3 / centena:8 / milhar: 1
num = int(input('Digite um número de 0 a 9999: '))
unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhares = num // 1000 % 10
print('o número escolhido tem: {} unidades, {} dezenas, {} centenas e {} milhares'.format(unidades,dezenas,centenas,milhares))