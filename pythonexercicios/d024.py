# crie um programa que leia o nome da sua cidade e diga se ela começa ou não com a palavra 'santo'
city = input('Qual o nome da sua cidade?') .strip()
print(city[:5].upper() == 'SANTO')
