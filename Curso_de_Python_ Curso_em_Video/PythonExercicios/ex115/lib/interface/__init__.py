def leiaInt(mgn):
    while True:
        try:
            n = int(input(mgn))
        except (ValueError, TypeError):
            print('\033[031mErro: por favor, digite um número interio válido.\033[m')
        else:
            return n
            break


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc