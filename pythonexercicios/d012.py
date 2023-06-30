#Faça um algoritimo que leia o preço de um produto e mostre o novo preço com desconto de 5%.
p = float(input('Qual o preço do produto? '))
np = (p-(p*0.05))
print('O produto de valor R${:.2f}, na promoção está saindo por R${:.2f}.'.format(p, np))
