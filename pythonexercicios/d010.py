#Cria um programa que leia quanto dinehiro tem na carteira e mostre quantos dolares ela consegue comprar, sendo que 1 us = 3,27 reais.

r = float(input('Quantos reais vc tem? '))
d = (r/3.27)
print('Com R${:.2f}, você consegue comprar U${:.2f}.'.format(r,d))
