from random import choice
from time import sleep
jokenpo = ['Pedra', 'Papel', 'Tesoura']
computador = choice(jokenpo)
jogador = str(input('Pedra, Papel ou Tesoura: '))
jogador = jogador.title()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == jogador:
    print('Você jogou {} e o Computador jogou {}'.format(jogador, computador))
    print()
    print('Empate!')
elif jogador == 'Pedra' and computador == 'Tesoura' or jogador == 'Papel' and computador == 'Pedra' or jogador == 'Tesoura' and computador == 'Papel':
    print('Você jogou {} e o Computador jogou {}'.format(jogador, computador))
    print()
    print('Parabéns você é o vencedor!')
elif computador == 'Pedra' and jogador == 'Tesoura' or computador == 'Papel' and jogador == 'Pedra' or computador == 'Tesoura' and jogador == 'Papel':
    print('Você jogou {} e o Computador jogou {}'.format(jogador, computador))
    print()
    print('Você perdeu!')
else:
    print('Opção inválida!!!')
