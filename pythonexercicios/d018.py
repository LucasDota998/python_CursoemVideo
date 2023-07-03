#Faca um programa que leia um angulo qualquer e mostre na tela o
#valor do seno, cosseno e tangente desse angulo
import math
ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('para o ângulo {}, temos o seno igual a {:.2f}, o cosseno igual a {:.2f} e a tangente igual a {:.2f}'.format(ang,sen , cos, tan))
