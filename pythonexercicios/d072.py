"""Crie uma programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
Seu proograma deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo na tela por extenso"""
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze'
            , 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente, deve ser um número entre 0 e 20')
print(f'Voce digitou o número {contagem[n]}.')
