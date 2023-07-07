#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da
#passagem, cobrando 0,50 reais por km para um viagem de até 200km e 0,45 para viagens mais longas
d = float(input('Qual a distancia em KM da sua viagem: '))

if d < 200:
    valor = d * 0.5
    print('Sua passagem custará: R${:.2f}'.format(valor))
else:
    valor = d * 0.45
    print('Sua passagem custará: R${:.2f}'.format(valor))
