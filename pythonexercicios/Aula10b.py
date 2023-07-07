n1 = float(input('QUal foi sua primeira nota: '))
n2 = float(input('Qual foi sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi de {}'.format(m))
if m >= 6:
    print('Você passou de ano, parabéns')
else:
    print('Infelizmente vc reprovou')
