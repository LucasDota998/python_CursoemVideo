#Crie um algoritimo que leia um número e mostre o seu dobro, tripo e raiz quadrada na tela.
n = int(input('Digite um número: '))
n2 = (n * 2)
n3 = (n * 3)
nq = (n**(1/2))
print('O numero {} tem seu dobro como {}, seu tripo como {} e sua raiz quadrada como {}'.format(n, n2, n3, nq))