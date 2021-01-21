numeros = [[], [], []]
somapares = somacoluna3 = 0
for va in range(0,len(numeros)):
    for v in range(0, 3):
        numeros[va].append(int(input(f'Digite um valor para a posição [{va}, {v}] ')))
        if numeros[va][v] % 2 == 0:
            somapares += numeros[va][v]
    if numeros[va][2]:
        somacoluna3 += numeros[va][2]
print('-=-' * 30)
print()
for valor in numeros:
    print(f'[ {valor[0]} ] [ {valor[1]} ] [ {valor[2]} ]')
print()
print('-=-' * 30)

print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somacoluna3}')
print(f'O maior valor da segunda linha é {max(numeros[1])}')
