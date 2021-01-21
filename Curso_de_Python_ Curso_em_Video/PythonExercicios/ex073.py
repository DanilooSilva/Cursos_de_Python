brasileirao = (
                'Flamengo',         'Santos',           'Palmeiras',
                'Grêmio',           'Athetico PR',      'São Paulo',
                'Internacional',    'Corinthians',      'Fortaleza',
                'Goiás',            'Bahia',            'Vasco',
                'Atlético MG',       'Fluminense',       'Botafogo',
                'Ceará',            'Cruzeiro',         'CSA',
                'Chapecoense',      'Avaí'
            )
print('-=-' * 30)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=-' * 30)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-=-' * 30)
print(f'Times em orderm alfabética: {sorted(brasileirao)}')
print('-=-' * 30)
print(f'Chapecoense esta na {brasileirao.index("Chapecoense") + 1}ª posição')