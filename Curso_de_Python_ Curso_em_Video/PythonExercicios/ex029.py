#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado! você excedeu o limite permitido de 80Km/h.')
    print('Você deve para uma multa de R$ {:.2f}!'.format(multa))


print('Tenha um bom dia! Dirija com segurança! ')