"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o o IMC e mostre se status:
-Abaixo de 18.5: ABaixo do peso
-Entre 18.5 e 25:Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade Morbida"""

p = float(input('Qual o seu peso: '))
a = float(input('Qual a sua altura: '))
imc = p / (a**2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Vc está ABAIXO DO PESO')
elif 18.6 < imc <= 25:
    print('Vc está no PESO IDEAL')
elif 25.1 < imc <= 30:
    print('Vc está com SOBREPESO')
elif 30.1 < imc <= 40:
    print('Vc está com OBESIDADE')
else:
    print('Vc está OBESO MORBIDO')
