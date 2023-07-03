#Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
catad = int(input('Digite o cateto adjacente: '))
catop = int(input('Digite o cateto oposto: '))
hip = math.hypot(catop, catad)
print('A hipotenusa irá medir: {:.2f}'.format(hip))


