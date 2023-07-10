#Condições Aninhadas
nome = str(input('Digite seu nome: '))
if nome == 'Lucas':
    print('Seu nome é muito bonito')
elif nome == 'Pedro' or nome == 'Joao' or nome == 'Luiza':
    print('Seu nome é bem comum no Brasil')
elif nome == 'Creuza' or nome == 'Kelen' or nome == 'Stefany':
    print('Voce tem um nome bosta')
else:
    print('Seu nome é bem normal')
print('Prazer em te conhecer, {}'.format(nome))
