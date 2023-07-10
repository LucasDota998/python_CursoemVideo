#Faça um programa que leia um número inteiro e mostre na tela o seu sucessesor e seu antecessor
n = int(input('Digite um número:'))
ns = (n + 1)
na = (n - 1)
print('O sucessor do numero é \033[32m{}\033[m e o antecessor do número é \033[31m{}\033[m'.format(ns, na))
