try:
    arquivo = open('pessoa.csv')

    for registro in arquivo:
        registro = registro.split(',')
        print(f'Nome: {registro[0]}, Idade: {registro[1].strip()} anos')
except:
    print('Aconteceu algo de errado! ')
finally:
    arquivo.close()