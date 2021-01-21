arquivo = open('pessoa.csv') # abrindo arquivo
dados = arquivo.read() # fazendo leitura e armazenando dados do arquivo na variavel
arquivo.close() # fechando arquivo

for registro in dados.splitlines():
    registro = registro.split(',')
    print(f'Nome: {registro[0]}, Idade: {registro[1]} anos')

