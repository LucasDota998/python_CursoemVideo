"""n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('PAR: {} '.format(par))
print('Impar: {} '.format(impar))"""
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N]: ')).upper()
print('Fim')