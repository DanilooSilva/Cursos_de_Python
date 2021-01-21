def aumentar(v, p=10, f=False):
    res = v + (v * p / 100)
    if f:
        return moeda(v=res)
    else:
        return res


def diminuir(v=0, p=13, f=False):
    res = v - (v * p / 100)
    if f:
        return moeda(v=res)
    else:
        return res


def dobro(v=0, f=False):
    res = v * 2
    if f:
        return moeda(v=res)
    else:
        return res


def metade(v=0, f=False):
    res = v / 2
    if f:
        return moeda(v=res)
    else:
        return res


def moeda(v=0, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')


def resumo(v=0, aP=10, dP=13):
    print('--' * 20)
    print(F'{"RESUMO DO VALOR":^40}')
    print('--' * 20)
    print(f'{"Preço analisado:":<25} {str(moeda(v))}')
    print(f'{"A metade do preço:":<24}  {metade(v, True)}')
    print(f'{"O dobro do preço:":<25} {dobro(v, True)}')
    print(f'{str(aP) + "% de aumento:":<25} {aumentar(v, aP, f=True)}')
    print(f'{str(dP) + "% de redução:":<25} {diminuir(v, dP, f=True)}')
    print('--' * 20)