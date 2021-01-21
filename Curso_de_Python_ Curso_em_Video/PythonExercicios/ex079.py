valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if con in 'N':
        break
print('-=-' * 30)
valores.sort()
print(f'Voce digitou os valores {valores}')