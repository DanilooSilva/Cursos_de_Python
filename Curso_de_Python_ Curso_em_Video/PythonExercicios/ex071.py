print('=' * 30)
print('{:^30}'.format(' Banco CEV '))
print('=' * 30)
valor = int(input('Que valor quer sacar ? R$ '))
cedulas = 50
totalCedulas = 0
valorTotal = valor
while True:
    if valorTotal >= cedulas:
        valorTotal -= cedulas
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} células de R$ {cedulas:.2f}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalCedulas = 0
        if valorTotal == 0:
            break
print('=' * 30)
print('{:^30}'.format(' Volte Sempre ao Banco Curso em video. Tenha um Bom dia!'))