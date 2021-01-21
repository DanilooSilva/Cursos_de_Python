from datetime import date

anoAtual = date.today().year
anoNasci = int(input('Digite o ano de nascimento: '))
idade = anoAtual - anoNasci

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
else:
    print('Master')