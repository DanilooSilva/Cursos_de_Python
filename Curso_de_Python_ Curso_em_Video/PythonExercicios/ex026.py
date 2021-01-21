#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).strip()
frase = f.upper()
print('A letre A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))