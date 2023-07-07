#Escreve um programa que leia a velociade de um carro,
#se ele ultrapassar a velocidade maxima de 80km/h, mostre
#uma mensagem dizendo que ele foi multado
#A multa vai custar 7 reais por km acima do limite
vel = float(input('Em qual velocidade vc passou: '))

if vel > 80:
    print('Vc foi MULTADO')
    multa = (vel-80)*7
    print('Sua multa vai custar: R${:.2f}'.format(multa))
else:
    print('Ta tranquilo, vc não foi multado')
print('Dirija com segurança.')
