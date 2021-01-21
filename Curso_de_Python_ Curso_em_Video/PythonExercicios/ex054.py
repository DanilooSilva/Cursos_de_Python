#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year
contMenor = 0
contMaior = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if anoAtual - nasc < 18:
        contMenor += 1
    else:
        contMaior += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(contMaior))
print('E também {} pessoas menores de idade'.format((contMenor)))