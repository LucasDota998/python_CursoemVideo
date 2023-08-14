"""Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares em uma, e os valores impares na outra.
No final, mostre o conteúdo das três listas geradas"""
lista = list()
listapar = list()
listaimpar = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    r = str(input('Deseja continuar [S/N]: ')).upper()
    if r == 'N':
        break
print(f'Foram digitados os valores: {lista}')
print(f'A lista de pares ficou com os números: {listapar}')
print(f'A lista de números impares ficou com os números: {listaimpar}')