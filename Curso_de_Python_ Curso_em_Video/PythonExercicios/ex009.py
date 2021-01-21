#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para ver sua tabuada: '))
result = 0
cont = 0
print('=' * 12)
while cont <= 10:
    result = n * cont
    print('{} x {:2} = {}'.format(n, cont, result))
    cont += 1


print('=' * 12)