from random import randint
numero_tuplas = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1,20), randint(1,20))
maior = numero_tuplas[0]
menor = numero_tuplas[0]

print(f'Os valores sorteados foram: ', end='')
for numeros in numero_tuplas:
    print(numeros, end=' ')

for n in range(0, len(numero_tuplas)):
    if numero_tuplas[n] > maior:
        maior = numero_tuplas[n]
    if numero_tuplas[n] < menor:
        menor = numero_tuplas[n]
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
