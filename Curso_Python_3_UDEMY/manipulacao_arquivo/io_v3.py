arquivo = open('pessoa.csv')

for registro in arquivo:
    registro = registro.split(',')
    print(f'Nome: {registro[0]}, Idade: {registro[1].strip()} anos')

arquivo.close()