"""
Zip - Unindo iteráveis
Zip_longest _ Itertools
"""
from itertools import zip_longest, count

index = count()
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(cidades, estados)

for valor in cidades_estados:
    print(valor)