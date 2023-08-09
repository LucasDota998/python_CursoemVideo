"""Listas em Python
EX1
num = [2,4,6,5]
num[2] = 1
num.append(7)
num.sort()
num.insert(3,8)
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos')"""

"""EX2
valores = []
valores.append(5)
valores.append(2)
valores.append(7)

for c,v in enumerate(valores):
    print(f'Na posição {c} temos o valor {v}')
print('Fim da lista')"""

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'Na posição {c} temos o valor {v}')
print('Fim da lista')