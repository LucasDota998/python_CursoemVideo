# escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a 1250 reias, o aumento será de 10%
#Para salarios inferiores ou iguais, o aumento é de 15%
sal = float(input('Digite seu salário: '))
if sal < 1250:
    sal = sal + (sal*0.15)
    print('O seu novo salário será de: R${:.2f}'.format(sal))
else:
    sal = sal + (sal*0.1)
    print('O seu novo salário será de: R${:.2f}'.format(sal))
