from random import randint
from time import sleep

print('-=-' * 40)
print('TENTE ADIVIDANHA QUAL NÚMERO O COMPUTADOR PENSOU DE 0 a 10')
print('-=-'* 40)

pc = randint(0, 10)
pess = int(input('Digite o número: '))
cont = 0

print('Processando!')
sleep(2)


while pess != pc:
    pess = int(input('Digite o número: '))
    cont += 1
print('Parabéns você acertou e precisou de {} palpites para conseguir.'.format(cont))