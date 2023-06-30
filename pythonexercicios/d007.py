# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = input('Qual o seu nome?')
n1 = float(input('Qual sua primeira nota?'))
n2 = float(input('Qual sua segunda nota?'))
m = ((n1 + n2)/2)
print('O aluno {}, tirou {} na primeira prova, {} na segunda prova, portanto sua média é {}'.format(nome, n1, n2, m))