cont = 0
listaDeNumeros = list()
while True:
    cont += 1
    numeros = int(input(f'Digite {cont}° número: '))
    listaDeNumeros.append(numeros)
    continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=-' * 30)
print(f'Voce digitou {cont} elementos')
listaDeNumeros.sort(reverse=True)
print(f'Os valores em order decrescente {listaDeNumeros}')
print('O valor 5 faz parte da lista' if 5 in listaDeNumeros else 'O valor 5 não faz parte da lista')
