frase = input('Digite uma frase: ')
print('A letra "A" aparece {}'.format(frase.upper().count('A')))
print('A aparece a primeira vez na posição {} '.format(frase.lower().find('a')))
print('A aparece a ultima vez na posição {}'.format(frase.upper().rfind(('A'))))

