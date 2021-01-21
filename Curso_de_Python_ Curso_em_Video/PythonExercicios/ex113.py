def leiaInt(mgn):
    while True:
        try:
            n = int(input(mgn))
        except (ValueError, TypeError):
            print('\033[031mErro: por favor, digite um número interio válido.\033[m')
        else:
            return n
            break


def leiaFloat(mgn):
    while True:
        try:
            n = float(input(mgn))
        except (ValueError, TypeError):
            print('\033[031mErro: por favor, digite um número real válido.\033[m')
        else:
            return f'{n:.2f}'
            break




nu = leiaInt('Digite um valor inteiro: ')
fl = leiaFloat('Digite um número real: ')
print(f'O valor Inteiro é {nu} e o número real é {fl}')