def executa(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa tarde!')


if __name__ == '__main__':
    executa(bom_dia)
    executa(boa_tarde)
    executa(1)