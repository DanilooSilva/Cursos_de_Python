ano = int(input('Digite um ano: Ex(2020): '))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('O ano {} é um ano bixesto!'.format(ano))
else:
    print('O ano {} não é um ano bixesto!'.format(ano))