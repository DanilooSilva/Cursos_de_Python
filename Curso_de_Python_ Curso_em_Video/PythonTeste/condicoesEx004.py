d = float(input('Qual é a distância da viagem (km): '))

if d <= 200:
    print('O valor da passagem é: R$ {:.2f}.'.format(d * 0.5))
else:
    print('O valor da passagem é: R$ {:.2f}'.format(d * 0.45))

