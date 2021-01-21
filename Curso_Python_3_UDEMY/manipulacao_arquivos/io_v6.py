with open('pessoa.csv') as arquivo:
    with open('pessoa.txt', 'w') as saida: # with para abrir e fechar recursos do sistema operacinal
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print(f'Nome: {pessoa[0]} Idade: {pessoa[1]}', file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado!')