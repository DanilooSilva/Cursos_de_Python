#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um número qualquer: '))

print('O número {} é PAR'.format(numero) if numero % 2 == 0 else 'O número {} é IMPAR'.format(numero))

