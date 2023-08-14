"""Crie um programa onde o usuário possa digitar vários valores numericos e cadastre-os em uma lista.
Caso o numero já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores
unicos digitados, em ordem crescente"""
lista = list()
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não adicionado!')

    p = str(input('Deseja continuar[S/N]: ')).upper()
    if p in 'N':
        break
print(f'Os valores ineditos adicionas em ordem crescente são: {sorted(lista)}')


