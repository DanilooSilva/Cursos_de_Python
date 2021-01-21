from random import randint
from time import  sleep
numeros = list()



def sorteia(n):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        valores = randint(1, 9)
        print(f'{valores} ', end='')
        n.append(valores)
        sleep(0.5)
    print('Pronto!')


def somaPar(par):
    soma = 0
    for p in par:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores de {par}, temo {soma}')


sorteia(numeros)
somaPar(numeros)