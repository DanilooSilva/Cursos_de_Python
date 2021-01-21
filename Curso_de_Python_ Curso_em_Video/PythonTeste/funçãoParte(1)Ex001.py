def titulo(txt):
    print('-=' * 30)
    print(f'{txt.title():^60}')
    print('-=' * 30)


def area(largura, comprimento):
    aterreno = largura * comprimento
    print(f'A área de um terreno {largura:.1f}X{comprimento:.1f} é de {aterreno:.1f}m².')


titulo('Contole de terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
