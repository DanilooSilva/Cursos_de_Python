#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Sua opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

computador = randint(0, 1)
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if jogada == computador:
    print('Empate')
elif jogada == 1 and computador == 2 or jogada == 2 and computador == 3 or jogada == 2 and computador == 3 or jogada == 3 and computador == 1:
    print('Você perdeu tente novamente! ')
elif computador == 1 and jogada == 2 or computador == 2 and jogada == 3 or computador == 2 and jogada == 3 or computador == 3 and jogada == 1:
    print('Você ganhou! Parabéns!')
else:
    print('Opção inválida! ')

print()
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogada]))