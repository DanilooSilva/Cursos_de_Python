from datetime import date

anoNascimento = int(input('Digite o ano de seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 17:
    print('Você ainda vai se alistar no serviços militar.')
    print('Falta {} ano(s) para seu alistamento.'.format(18 - idade))
elif idade == 18:
    print('Chegou a hora do alistamento militar.')
else:
    print('Já passou da hora de se alistar no serviços militar.')
    print('Já passou {} ano(s) do seu alistamento.'.format((idade - 18)))
