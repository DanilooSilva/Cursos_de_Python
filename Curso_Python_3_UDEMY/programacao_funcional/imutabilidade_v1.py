#! python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
meses_com_31_dia = filter(lambda m: mdays[m] == 31, range(1, 13))
nome_meses = map(lambda m: month_name[m].title(), meses_com_31_dia)
juntar_meses = reduce(lambda todos, nome_mese: f'{todos}\n {nome_mese}', nome_meses, 'Meses com 31 dias: ')
print(juntar_meses)