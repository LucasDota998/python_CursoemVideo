"""Crie um programa que faça o computador jogar jokenpô com vc """
import random
from time import sleep
eu = str(input('''======JOKEEEEEEN-PO:======  
Escolha uma opção:
==pedra==
==papel==
==tesoura==
Sua opção: '''))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)

if eu == pc:
    print('EMPATOU')
elif eu == 'pedra' and pc == 'papel':
    print('VC PERDEU!!')
elif eu == 'papel' and pc == 'pedra':
    print('VC GANHOOOU!!')
elif eu == 'pedra' and pc == 'tesoura':
    print('VC GANHOOOU!!')
elif eu == 'tesoura' and pc == 'pedra':
    print('VC PERDEUU')
elif eu == 'papel' and pc == 'tesoura':
    print('VC PERDEU!')
elif eu == 'tesoura' and pc == 'papel':
    print('VC GANHOU!')
else:
    print('Nome inválido, tente novamente')
print('Eu escolhi {}'.format(pc))