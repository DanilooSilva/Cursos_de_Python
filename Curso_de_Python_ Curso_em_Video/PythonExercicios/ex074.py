from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = numeros[0]
menor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print(f'Os valore sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')