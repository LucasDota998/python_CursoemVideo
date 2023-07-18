"""Crie um programa que leia dois valores e mostre um menu na tela:
1 - somar
2 - multiplicar
3 - maior
4 - novos numeros
5 - sair
Seu programa deverá realizar a operação solicitada em cada caso"""
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    print('''Escolha o próximo passo:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))

    elif escolha == 2:
        produto = n1 * n2
        print('O produto entre {} x {} = {}'.format(n1, n2, produto))

    elif escolha == 3:
        if n1 > n2:
            print('{} é o MAIOR'.format(n1))
        else:
            print('{} é o MAIOR'.format(n2))

    elif escolha == 4:
        print('Informe os números novamente...')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Jogo finalizado com sucesso!')

