from datetime import date

anoAtual = date.today().year
contMaior = 0
contMenor = 0

for c in range(1, 8):
    dataNasc = int(input('Digite a data de nascimento: '))
    if anoAtual - dataNasc >= 18:
        contMaior += 1
    else:
        contMenor += 1

print('{} pessoa são maiores de 18 anos e {} pessoas são menores de 18 anos'.format(contMaior, contMenor))