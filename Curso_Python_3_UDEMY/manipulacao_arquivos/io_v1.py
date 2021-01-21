arquivo = open('pessoa.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    registro = registro.split(',')
    print(f'Nome: {registro[0]}, Idade: {registro[1]}')