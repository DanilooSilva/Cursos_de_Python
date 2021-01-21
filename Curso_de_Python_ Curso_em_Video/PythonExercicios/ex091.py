from random import  randint
from operator import itemgetter
from time import sleep

jogador = {}
ranking = []

for i in range(1, 5):
    jogador[f'jogador{i}'] = randint(1,6)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse= True)
print('Valores Sorteados:')
for c, j in jogador.items():
    print(f'{c} tirou {j} no dado')
    sleep(1)
print('-=' * 30)
print('{:>5} {:^10} {:<5}'.format('=' * 2, 'Ranking dos jogadores', '=' * 2))
for c, r in enumerate(ranking):
    print(f'{c + 1:>5}{"° lugar:"} {r[0]} com {r[1]}.')

