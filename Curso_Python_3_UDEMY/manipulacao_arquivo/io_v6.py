with open('pessoa.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            registro = registro.strip().split(',')
            print(f'Nome:{registro[0]}, Idade: {registro[1]} anos', file=saida)