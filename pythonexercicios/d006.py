#Crie um algoritimo que leia um número e mostre o seu dobro, tripo e raiz quadrada na tela.
n = int(input('Digite um número: '))
n2 = (n * 2)
n3 = (n * 3)
nq = (n**(1/2))
print('O numero \033[34m{}\033[m tem seu dobro como \033[4;31m{}\033[m, seu tripo como \033[4;36m{}\033[m e sua '
      'raiz quadrada como \033[4;33m{:.2f}\033[m'.format(n, n2, n3, nq))