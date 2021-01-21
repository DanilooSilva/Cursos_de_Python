valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for index, valor in enumerate(valores):
    print(f'Na posição {index + 1} encontrei o valor {valor}!')
print('Chequei ao final da lista.')