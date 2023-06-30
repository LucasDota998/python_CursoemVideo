#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com um aumento de 15%.
s = float(input('Qual o seu salário? '))
ns = (s+(s*0.15))
print('O seu salário atual é de R${:.2f}, mas com o reajuste irá para R${:.2f}'.format(s, ns))
