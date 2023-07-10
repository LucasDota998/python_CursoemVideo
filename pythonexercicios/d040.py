"""Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a
 média atingida:
 -Média abaixo de 5.0: REPROVADO
 -Média entre 5.0 e 6.9: RECUPERAÇÃO
 -Média 7.0 ou superior: APROVADO"""
n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
m = (n1 + n2)/2
if m <= 5:
    print('Vc está \033[31mREPROVADO!!!')
elif 5 < m < 6.9:
    print('Vc está de \033[33mRECUPERAÇÃO!!!')
else:
    print('\033[32mPARABENS, vc está APROVADO!!!')
print('Sua média foi de {:.2f}'.format(m))
