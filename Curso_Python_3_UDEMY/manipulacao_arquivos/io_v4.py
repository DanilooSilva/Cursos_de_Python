try:
    arquivo = open('pessoa.csv')
    for registro in arquivo:
        registro.split(',')
        print(f'Nome: {registro.split(",")[0]}, Idade: {registro.strip().split(",")[1]}')
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado')
