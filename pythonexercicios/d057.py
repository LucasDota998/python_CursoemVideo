"""Faca um programa que leia o sexo de uma pessoa, mas só aceite os valores 'F' ou 'M'.
Caso esteja errado, peça a digitação novamente até ter uma valor correto."""

sexo = str(input('Informe se sexo [M/F]: ')).strip() .upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Informe novamente: ')) .strip() .upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))




