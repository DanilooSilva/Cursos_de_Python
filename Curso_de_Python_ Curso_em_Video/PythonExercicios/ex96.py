print('Controle de Terrenos')
print('--' * 30)


def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}X{c:.1f} é de {a:.1f}m².')


lag = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(lag, comp)
