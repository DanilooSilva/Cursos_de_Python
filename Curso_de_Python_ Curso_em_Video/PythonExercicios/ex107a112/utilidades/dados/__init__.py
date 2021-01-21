def leiaDienheiro(msg):
    while True:
        leia = str(input(msg))
        if leia.replace(',', '').replace('.', '').isdigit():
            valor = leia.replace(',', '.')
            return float(valor)
            break
        else:
            print(f'\033[031mERRO! \'{leia}\' é um preço inválido!\033[m')