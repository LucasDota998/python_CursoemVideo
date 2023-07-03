# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
# a diária é 60 reias e o km rodado é 0,15 centavos
dias = int(input('Qual o número de dias alugados: '))
km = int(input('Quantos kms foram rodados: '))
total = (dias*60) + (km*0.15)
print('Diárias: {}'.format(dias))
print('Km rodados: {}'.format(km))
print('O total a ser pago é: R${:.2f}'.format(total))