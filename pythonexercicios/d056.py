"""Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final, mostre:
A média da idade do grupo;
Qual é o nome do homem mais velho
Quantas mulheres tem menos de 20 anos"""
somaidade = 0
mediaidade = 0
idadevelho = 0
nomevelho = ''
totalmulhernova = 0
for p in range(1, 5):
    print('-------- {}a PESSOA --------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 18:
        totalmulhernova += 1

mediaidade = somaidade/4
print('A média entre as idade é: {}'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, idadevelho))
print('Ao todo temos {} mulher(es) menores de idade.'.format(totalmulhernova))