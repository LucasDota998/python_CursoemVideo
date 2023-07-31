"""Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A - Quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - Quantas mulheres tem menos de 20 anos"""
maior = 0
homens = 0
fmenor = 0
while True:
    add = str(input('Deseja adicionar uma pessoa [S/N]: ')).strip() .upper()
    if add == 'S':
        idade = int(input('Qual a idade: '))
        sexo = str(input('Qual o sexo [M/F]: ')).strip() .upper()
    else:
        print('Cadastro encerrado!')
        break
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        fmenor += 1
print(f'Com a maioridade temos {maior} pessoas. Foram cadastrados {homens} homens e das mulheres {fmenor} '
      f'tem menos de 20 anos')
