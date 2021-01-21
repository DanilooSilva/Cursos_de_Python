arquivo = open('pessoa.csv')
for registro in arquivo:
    registro.split(',')
    print(f'Nome: {registro.split(",")[0]}, Idade: {registro.split(",")[1]}', end='')
arquivo.close()