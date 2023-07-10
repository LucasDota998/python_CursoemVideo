# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
cores = {'limpa': '\033[m',
         'verm': '\033[31m',
         'verde': '\033[32m',
         'azul': '\033[34m'}
nome = input('Qual o seu nome?')
n1 = float(input('Qual sua primeira nota?'))
n2 = float(input('Qual sua segunda nota?'))
m = ((n1 + n2)/2)
print('O aluno {}{}{}, tirou {}{}{} na primeira prova, {}{}{} na segunda prova, portanto sua média é {}{}{}'
      .format(cores['azul'], nome, cores['limpa'],cores['verm'],n1, cores['limpa'],cores['verm'], n2,cores['limpa'],cores['verde'], m,cores['limpa'] ))