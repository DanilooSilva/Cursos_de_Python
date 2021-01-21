def leiaDinheiro(mgn):
    while True:
        valor = str(input(mgn))
        if valor.replace(',', '').isdigit():
            valorcorreto = float(valor.replace(',', '.'))
            return float(valorcorreto)
            break
        else:
            print(f'\033[31mErro! \"{valor.replace(",", ".")}\" é um preço inválido!\033[m')