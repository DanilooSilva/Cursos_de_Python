# Exercício Python 028: Escreva um programa que faça o computador
# "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=-' * 50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhas... ')
print('-=-' * 50)

npc = randint(0, 5)
nu = int(input('Digite o número: '))

print('Processando!')
sleep(3)

if nu == npc:
    print('Parabens você venceu! ')
else:
    print('Ganhei! Pensei no número {} e não no {}'.format(npc, nu))
