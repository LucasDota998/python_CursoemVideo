"""Crie um programa que tenha uma tupla com varias palavras(não usar acentos). Ddepois disso, voce deve mostrar,
para cada palavra, quais são as suas vogais"""
palavras = ('aço', 'cobre','aluminio','ferro', 'ouro','platina','latao','niquel','prata')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos tais vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')