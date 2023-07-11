"""Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final,
mostre os 10 primeiros termos dessa progressão"""
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
for c in range(t, (t+r*10), +r):
    print(c)


