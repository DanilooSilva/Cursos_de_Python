import random

numeroPc = random.randint(1, 5)
numeroUsuario = int(input('Digite um número: '))


print('Parabéns vc acertou!' if numeroPc == numeroUsuario else 'O Computador venceu')
