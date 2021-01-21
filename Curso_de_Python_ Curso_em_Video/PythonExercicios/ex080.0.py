valores = []
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if cont == 0:
        print('Adicionado ao final da lista...')
        valores.append(valor)
    else:
        if valores[0] >= valor:
            valores.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
        elif valores[-1] <= valor:
            valores.append(valor)
            print('Adicionado ao final da lista...')
        elif valores[1] >= valor:
            valores.insert(1, valor)
            print('Adicionado na posição 1 da lista...')
        elif valores[2] >= valor:
            valores.insert(2, valor)
            print('Adicionado na posição 2 da lista...')
        elif valores[3] >= valor:
            valores.insert(3, valor)
            print('Adicionado na posição 3 da lista...')
        elif valores[4] >= valor:
            valores.insert(4, valor)
            print('Adicionado na posição 4 da lista...')
print('-=-' * 30)
print(f'Os valores digitados em ordem foram {valores}')