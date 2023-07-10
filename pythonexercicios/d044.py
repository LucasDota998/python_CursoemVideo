"""Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e
consição de pagamento:

-à vista dinheiro: 10% de desconto
- a vista no cartão: 5% de desconto
- em 2x: preço normal
- acima de 3 x: 20% de juros"""

preco = float(input('Qual o valor do produto: '))
print('''Escolha uma das formas de pagamento:
[ 1 ] À vista no dinheiro (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] Parcelado em 2X (preço normal)
[ 4 ] Parcelado em 3X ou mais (acrescimo de juros)''')
op = int(input('Sua opção: '))

if op == 1:
    print('À vista no dinheiro o produto sai por: R${:.2f}'.format(preco - (0.1*preco)))
elif op == 2:
    print('À vista no cartão o produto sai por: R${:.2f}'.format(preco - (0.05 * preco)))
elif op == 3:
    print('Parcelado em duas vezes sai por: R${:.2f}'.format(preco))
elif op == 4:
    print('Parcelado acima de 3x o produto sai por: R${:.2f}'.format(preco + (preco * 0.2)))
else:
    print('Opção inválida. Tente novamente!')




