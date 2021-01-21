sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while not sexo in 'MF':
    print('Sexo não existente favor digitar Novamente! ')
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()