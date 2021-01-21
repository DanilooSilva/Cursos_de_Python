brasileirao = (
                'Flamengo',         'Santos',           'Palmeiras',
                'Grêmio',           'Athetico PR',      'São Paulo',
                'Internacional',    'Corinthians',      'Fortaleza',
                'Goiás',            'Bahia',            'Vasco',
                'Atlético MG',       'Fluminense',       'Botafogo',
                'Ceará',            'Cruzeiro',         'CSA',
                'Chapecoense',      'Avaí'
            )
print('-' * 30)
print('Os 5 primeiros colocados')
print('-' * 30)
for posi, primeiroquinto in enumerate(brasileirao[0:5]):
    print(f'{posi + 1} - {primeiroquinto}')
print('-' * 30)
print('Os quatros Ultimos colocados')
print('-' * 30)
for pos in range(16, len(brasileirao)):
    print(f'{pos + 1} - {brasileirao[pos]}')
print('-' * 30)
print('Clubes em ordem Alfabetica')
print('-' * 30)
ordemalpha = sorted(brasileirao)
for ordem in ordemalpha:
    print(ordem)

print()
print(f'A Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição')
