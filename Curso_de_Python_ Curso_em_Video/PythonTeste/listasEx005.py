numeros = list()
numerosPares = list()
numerosImpares = list()
while True:
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    continuar = str(input('Continuar ? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar ? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
for par in numeros:
    if par % 2 == 0:
        numerosPares.append(par)
for impar in numeros:
    if impar % 2 == 1:
        numerosImpares.append(impar)
print('-=-' * 30)
print(f'A lista comleta é {numeros}')
print(f'A lista de pares é {numerosPares}')
print(f'A lista de impares é {numerosImpares}')