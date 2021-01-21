#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

c = str(input('Qual cidade nasceu: ')).strip()
ci = 'Santo'
print(ci.upper() in c.upper())