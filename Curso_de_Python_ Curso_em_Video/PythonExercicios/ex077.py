nomes = ('Danilo', 'Maria', 'Ohara', 'Scarlett', 'Allanys')

for nome in nomes:
    print(f'Na palavra {nome.upper()} temos ', end='')
    for vogais in nome:
        if vogais in 'AaEeIiOoUu':
            print(f'{vogais}', end=' ')
    print()