def metade(n, f=False):
    if f:
        return f'{moedas(n / 2)}'
    else:
        return n / 2


def dobro(n, f=False):
    if f:
        return f'{moedas(n * 2)}'
    else:
        return  n * 2


def aumentar(n, p=10, f=False):
    if f:
        return f'{moedas(n + (n * p / 100))}'
    else:
        return n + (n * p / 100)


def diminuir(n, p=13, f=False):
    if f:
        return f'{moedas(n - (n * p / 100))}'
    else:
        return n - (n * p / 100)


def moedas(f):
    return f'R${f:.2f}'.replace('.', ',')



def resumo(p, a, r):
    print('--' * 20)
    print(f'{"RESUMO DO VALOR":^30}')
    print('--' * 20)
    print(f'{"Preço Analisado":<25}: {moedas(p)}')
    print(f'{"Dobro do preço":<25}: {dobro(p, True)}')
    print(f'{"Metade do preço":<25}: {metade(p, True)}')
    print(f'{str(a) + "% de Aumento":<25}: {aumentar(p, a, True)}')
    print(f'{str(r) + "% de Redução":<25}: {diminuir(p, r, True)}')
    print('__' * 20)