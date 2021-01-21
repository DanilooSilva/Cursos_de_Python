from random import randint
from operator import itemgetter
from time import sleep
jogadores = {}
ranking = {}
print('Valores sorteados:')
for j in range(1, 5):
    jogadores[f'jogador{j}'] = randint(1,6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'{i}° lugar: {v[0]} com {v[1]}')
    sleep(1)

