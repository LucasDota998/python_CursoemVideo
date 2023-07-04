# Crie um programa que leia o nome completo de uma pessoa e mostre:
#nome com letras maiusculas
#nome aotodo com minusculas
#quantas letras aotodo sem considerar espaços
#quantas letras tem o primeiro nome
nome = input('Diga o seu nome completo:').strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
nome = nome.split()
print(len(nome[0]))