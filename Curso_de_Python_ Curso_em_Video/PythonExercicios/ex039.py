#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Ano de nascimento: '))

idade = anoAtual - anoNasc

print('Quem nasceu em {} tem {} anos em {}'.format(anoNasc, idade, anoAtual))

if idade <= 17:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(18 - idade + anoAtual))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se aistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anoAtual - (idade - 18)))
