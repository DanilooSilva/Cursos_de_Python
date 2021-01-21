nomes = ('Danilo', 'Maria', 'Scarlett', 'Ohara', 'Allanys', 'Mel', 'Ze Russo')

for nome in nomes:
    print(f'No nome {nome.upper()} temos as vogais', end=' ')
    for vogais in nome:
        if vogais in 'aAeEiIoOuU':
            print(vogais, end=' ')
    print()