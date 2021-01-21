def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: {opcional} Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show == True:
        print(f'{n}', end='')
        for c in range(n, 0, -1):
            f *= c
            if c < n:
                print(f' x {c}', end='')
        print(' = ', end='')
    else:
        for c in range(n, 0, -1):
            f *= c
    return f


print(fatorial(10, True))