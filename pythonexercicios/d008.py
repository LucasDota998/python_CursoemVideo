#Escreva um programa que leia um valor em metros e o exiba convertido para centrimetos e milimetros.
m = float(input('Digite o valor em metros: '))
cm = (m*100)
mm = (m*1000)
print('O medida {}m, convertida para centímetros é {}cm e convertida para milímetros é {}mm'.format(m, cm, mm))