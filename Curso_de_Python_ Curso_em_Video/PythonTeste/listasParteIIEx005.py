from random import randint
from time import sleep

print('-' * 50)
print('{:^50}'.format('JOGOS DA MEGA SENA'))
print('-' * 50)
qntJogos = int(input('Quantos jogos quer que eu sorteie?: '))
jogos = list()
for c in range(0, qntJogos):
    sleep(1)
    numeros = list()
    cont = 0
    while True:
        numero = randint(1, 61)
        if numero not in numeros:
            numeros.append(numero)
            cont += 1
        if cont == 6:
            break


    jogos.append(numeros[:])
    numeros.clear()
    jogos[c].sort()
    print(f'Jogo {c + 1}: {jogos[c]}')