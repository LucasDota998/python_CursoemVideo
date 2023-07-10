"""Escreva um programa para aprovar o emprestimo bancário de compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
emprestimo será negado"""
casa = float(input('Qual o valor da casa que deseja adquirir: '))
sal = float(input('Qual a sua renda mensal: '))
anos = int(input('Em quantos anos vc quer pagar: '))
presta = casa / (anos*12)

print('Sua prestação vai ficar em: R${:.2f}'.format(presta))
if presta < (0.3*sal):
    print('Parabéns, seu emprestimo está \033[4:32mAUTORIZADO!!!')
else:
    print('Infelizmente seu emprestimo foi \033[4:31mNEGADO!!!')