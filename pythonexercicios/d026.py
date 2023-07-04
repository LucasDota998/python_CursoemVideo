#Faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra a
#em que posicao ela aparece a primeira vez
#em que posicao ela aparece da ultima vez
frase = str(input('Digite um frase: ')).upper().strip()
print(frase.count('A'))
print(frase.find('A'))
print('A ultima letra A apareceu na posição{}'.format(frase.rfind('A')))

