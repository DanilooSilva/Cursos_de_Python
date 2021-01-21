with open('pessoa.csv') as arquivo:
    for registro in arquivo:
        print(f'Nome: {registro.strip().split(",")[0]} Idade: {registro.strip().split(",")[1]}')

if arquivo.closed:
    print('Arquivo já foi fechado!')