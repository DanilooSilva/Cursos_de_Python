arquivo = open('pessoa.csv') # Abrindo arquivo
for registro in arquivo:
    registro = registro.split(',')
    print(f'Nome: {registro[0]} Idade: {registro[1]}', end='')
arquivo.close()