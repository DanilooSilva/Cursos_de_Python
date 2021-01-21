with open('pessoa.csv')  as arquivo:
    for registro in arquivo:
        registro = registro.strip().split(',')
        print(f'Nome: {registro[0]}, Idade: {registro[1]}')
