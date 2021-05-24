"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""
import json
import csv

with open(r'aula133\clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

with open(r'aula133\clientes.csv', 'w', newline='', ) as arquivo:
    escreve = csv.writer(
        arquivo,
        dialect=csv.excel_tab,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    chaves = list(dados['1'].keys())
    escreve.writerow(chaves)
    for dado in dados.values():
        escreve.writerow(
            [
                dado['nome'],
                dado['sobrenome'],
                dado['idade'],
                dado['altura'],
                dado['peso']
            ]
        )

with open(r'aula133\clientes.csv', 'r', newline='', ) as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

print(dados)            