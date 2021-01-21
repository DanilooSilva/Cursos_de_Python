listaValores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in listaValores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listaValores.append(valor)

    continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=-' * 30)
listaValores.sort()
print(f'Você digitou os valores {listaValores}')