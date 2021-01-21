contP = maiorPeso = menorPeso = 0
pessoas = list()
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    contP += 1
    continuar = str(input('Continuar?  [S/N]: ')).strip().upper()[0]
    while continuar not in 'NS':
        continuar = str(input('Continuar?  [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=-' * 30)
print(f'Ao todo, você cadastrou {contP} pessoas.')
for c in range(0, len(pessoas)):
    if c == 0:
        maiorPeso = pessoas[c][1]
        menorPeso = pessoas[c][1]
    else:
        if pessoas[c][1] > maiorPeso:
            maiorPeso = pessoas[c][1]
        if pessoas[c][1] < menorPeso:
            menorPeso = pessoas[c][1]
print(f'O maior peso foi de {maiorPeso} Kg. Peso de ', end='')
for p in pessoas:
    if maiorPeso == p[1]:
        print(f'{p[0]}... ', end='')
print()
print(f'O menor peso foi {menorPeso} Kg. Peso de ', end='')
for p in pessoas:
    if menorPeso == p[1]:
        print(f'{p[0]}... ', end='')
print()