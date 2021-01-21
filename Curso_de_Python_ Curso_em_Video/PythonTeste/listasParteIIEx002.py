lista = [[], []]
for c in range(0, 7):
    numero = int(input(f'Digite o {c + 1}° Número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('-=-' * 30)
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os valores ímpares digitados foram: {lista[1]}')