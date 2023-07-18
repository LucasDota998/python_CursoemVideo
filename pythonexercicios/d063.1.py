print('=' * 25)
print(' - Sequencia de Fibonaci - ')
print('=' * 25)
n = int(input('Digite quantos termos deseja ver da sequencia: '))
t1 = 0
t2 = 1
c = 3
mais = n
total = n
print('{} {} '.format(t1, t2), end='')
while mais != 0:
    total = total + mais
    while c <= total - n:
        t3 = t1 + t2
        print(' {} '.format(t3), end='')
        t1 = t2
        t2 = t3
        c += 1
    mais = int(input('Deseja ver mais quantos termos? '))
print(' - Progressão finalizada')