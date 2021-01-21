#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('''Sou seu Computador...
Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual foi?
''')
usuario = int(input('Qual é seu palpite: '))
pc = randint(0, 10)
cont = 1
while usuario != pc:
    if usuario < pc:
        print('Mais.. Tente mais uma vez.')
    elif usuario > pc:
        print('Menos... Tente novamente')
    usuario = int(input('Qual é seu palpite? '))
    cont += 1
print('Acertou com {} tentativas. Parabéns!'.format(cont))
