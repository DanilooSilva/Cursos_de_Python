pessoas = list()
dados = list()
maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=-' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso for de {maior_peso} Kg. peso de ', end='')
for pessoa in pessoas:
    if maior_peso == pessoa[1]:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor_peso} Kg. peso de ', end='')
for pessoa in pessoas:
    if menor_peso in pessoa:
        print(f'[{pessoa[0]}]', end=', ')