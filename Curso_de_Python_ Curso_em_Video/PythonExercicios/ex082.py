numeros = []
numerospares = []
numerosimpares = []
while True:
    numeros.append(int(input('Digite um número> ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
for num in numeros:
    if num % 2 == 0:
        numerospares.append(num)
    else:
        numerosimpares.append(num)
print(f'A lista complete é {numeros}')
print(f'A lista de pares é {numerospares}')
print(f'A list de ímpares é {numerosimpares}')