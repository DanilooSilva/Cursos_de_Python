lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=-' * 30)
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em orderm decrescente são {lista}')
print(f'O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 não faz parte da lista!')