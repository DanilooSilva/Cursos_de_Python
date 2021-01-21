numeros = [[], []]
nunaux = 0
for n in range(1, 8):
    nunaux = int(input(f'Digite o {n}°. valor: '))
    if nunaux % 2 == 0:
        numeros[0].append(nunaux)
    else:
        numeros[1].append(nunaux)
print('=-=' * 30)
numeros[0].sort()
print(f'Os números pares digitados foram: {numeros[0]}')
numeros[1].sort()
print(f'Os números ímpares digitados foram {numeros[1]}')