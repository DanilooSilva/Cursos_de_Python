arquivo = open('pessoa.csv')
for registro in arquivo:
    registro.split(',')
    print(f'Nome: {registro.split(",")[0]}, Idade: {registro.strip().split(",")[1]}')
arquivo.close()