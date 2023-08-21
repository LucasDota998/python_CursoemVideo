"""Listas dentro de listas
galera = [['Lucas', 32], ['Luiza', 31], ['Brisa', 4]]
print(galera[1][0])"""
galera = list()
dado = list()
menor = maior = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} tem {p[1]} anos')
        maior += 1
    else:
        print(f'{p[0]} tem {p[1]} anos ')
        menor += 1
print(f'Maiores de idade temos {maior} pessoas, e menores de idade temos {menor} pessoas')
