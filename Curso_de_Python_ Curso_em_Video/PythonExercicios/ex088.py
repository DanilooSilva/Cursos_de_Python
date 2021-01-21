from random import randint
from time import sleep
jogos = []
jogo = []
print('-' * 40)
print(f'{"Jogo na Mega Sena":^40}')
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"-=" * 5} Sorteando {qtd} Jogos {"-=" * 5}')
for j in range(0, qtd):
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            cont += 1
        if cont == 6:
            break
    jogos.append(jogo[:])
    jogo.clear()
    sleep(1)
    jogos[j].sort()
    print(f'Jogo {j + 1}: {jogos[j]}')
print(f'{"-=" * 6} < Boa Sorte > {"-=" * 6}')