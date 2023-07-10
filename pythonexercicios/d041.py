"""A confederação nacional de natação precisa de uma programa que leia o ano de nascimento de um atleta e mostrre
sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM
Até 14 anos: infantil
-Até 19 anos: junior
-Até 25 anos: Senior
-Acima: Master"""

from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento: '))
idade = atual - nasc
print('Vc tem {} anos'.format(idade))
if idade <= 9:
    print('Vc está na categoria MIRIM')
elif 9 < idade <= 14:
    print('Vc está na categoria INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria é a JUNIOR')
elif 19 < idade <= 25:
    print('Sua categoria é a SENIOR')
else:
    print('Vc está na categoria MASTER')
