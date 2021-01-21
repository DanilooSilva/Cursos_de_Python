import csv

with open('desafio-ibge.csv', encoding='ISO-8859-1') as arquivo:
    for informacoes in csv.reader(arquivo):
        print(f'{informacoes[8]}, {informacoes[3]}')