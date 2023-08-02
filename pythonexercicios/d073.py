"""Crie um tupla preenchida com os 10 primeiros colocados da tabela do campeonato brasileiro de futebol,
na ordem de colocação. Depois mostre:
A - Apenas os 5 primeiros colocados
B - Os 4 últimos colocados da tabela.
C - uma lista com os times em ordem alfabética
D - Em que posição na tabela está o time do palmeiras"""
times = ('Botafogo', 'Flamengo', 'Palmeiras','Grêmio', 'Fluminense', 'Bragantino', 'Atletico-PR', 'São Paulo', 'Cuiabá',
         'Cruzeiro')
print(f'Os 5 primeiro colocados são: {times[0:6]}')
print(f'Os 4 últimos colocados são: {times[6:]}')
print(f'Em ordem alfábetica dos times temos: {sorted(times)}')
print(f'O Palmeiras está na posição {times.index("Palmeiras")+1} da tabela')
