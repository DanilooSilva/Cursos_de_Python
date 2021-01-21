from random import randint
from time import sleep
numeros = []

def sorteia(lst):
    for i in range(0, 5):
         n = randint(0, 10)
         lst.append(n)
def somaPar(somalst):
    soma = 0
    for n in somalst:
        if n % 2 == 0:
            soma += n
    return soma


sorteia(numeros)
sleep(0.4)
print(f'Sorteando 5 valores de da lista: ', end='')
for v in numeros:
    sleep(0.4)
    print(f'{v} ', end='')
print('Pronto!')
sleep(0.4)
print(f'Somando dos valores pares de {numeros}, temos {somaPar(numeros)}')