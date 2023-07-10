"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar;
-Se é a hora de se alistar;
-Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que passou ou falta para o prazo de alistamento"""
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano vc nasceu: '))
idade = atual - nasc
tempo = (idade - 18)
if idade < 18:
    print('Ainda não está na hora de se alistar, faltam {} anos para seu alistamento'.format(tempo))
elif idade == 18:
    print('\033[32mEstá na hora de se alistar\033[m')
else:
    print('\033[31mJá passou da hora.\033[m Vc devia ter se alistado há {} anos'.format(tempo))
