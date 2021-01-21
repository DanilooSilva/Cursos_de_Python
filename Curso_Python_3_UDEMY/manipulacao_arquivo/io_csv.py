import csv
with open('pessoa.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print(f'Nome: {pessoa[0]}, Idade: {pessoa[1]}')