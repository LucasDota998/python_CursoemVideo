t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
termo = t
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'.format(termo))
        termo += r
        c += 1
    mais = int(input('Deseja mais quantos termos? '))
print('Fim')
