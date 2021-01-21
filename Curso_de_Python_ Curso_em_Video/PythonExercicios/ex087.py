matriz = [[], [], []]
somaPares = somaColuna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}][{c}]: ')))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    if matriz[l][2]:
        somaColuna3 += matriz[l][2]
print('=-' * 30)
for v in matriz:
    print(f'[{v[0]:^5}] [{v[1]:^5}] [{v[2]:^5}]')
print('-=' * 30)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaColuna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
