# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.
alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = (alt * lar)
tinta = (area/2)
print('Para pintar uma parede de {}m2, será necessário {}L de tinta.'.format(area, tinta))

