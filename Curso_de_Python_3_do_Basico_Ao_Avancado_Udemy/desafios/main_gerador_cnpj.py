from desafioValidaCNPJ import validador, get_CNPJ

if __name__ == '__main__':
    for i in range(100):
        cnpj_1 = get_CNPJ()
        print(f'{cnpj_1} e valido? {validador(cnpj_1)}')
