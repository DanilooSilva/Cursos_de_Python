numeros = list()
for num in range(0, 5):
    valor = int(input('Digite um valor: '))
    if num == 0:
        numeros.append(valor)
        print('Valor adicionado na última posição')
    else:
        if valor < numeros[0]:
            print('Numero adicionado na posição 0')
            numeros.insert(0, valor)
        elif valor > numeros[-1]:
            print('Valor adicionado na última posição')
            numeros.append(valor)
        elif valor < numeros[1]:
            print('Numero adicionado na posição 1')
            numeros.insert(1, valor)
        elif valor < numeros[2]:
            print('Numero adicionado na posição 2')
            numeros.insert(2, valor)
        elif valor < numeros[3]:
            print('Numero adicionado na posição 3')
            numeros.insert(3, valor)
        elif valor < numeros[4]:
            print('Número adicionado na posição 4')
            numeros.insert(4, valor)
print('-=-' * 30)
print(f'Os valores digitados em ordem froma {numeros}')