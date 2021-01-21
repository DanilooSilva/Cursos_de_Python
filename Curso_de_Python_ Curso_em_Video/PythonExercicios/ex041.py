#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Ano nascimento: '))
idade = anoAtual - anoNasc
print('O atleta tem {} anos'.format(idade))
if idade < 10:
    print('Mirim')
elif idade < 15:
    print('Infantil')
elif idade < 20:
    print('Junior')
elif idade < 25:
    print('Sênior')
else:
    print('Master')
