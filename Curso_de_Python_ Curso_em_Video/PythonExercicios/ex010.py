#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Quando dinheiro você tem na carteira? R$ '))
dolar = 5.06

conversor = reais / dolar

print('Com R$ {:.2f}  você pode comporar US$ {:.2f}'.format(reais, conversor))