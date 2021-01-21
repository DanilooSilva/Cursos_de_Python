matriz = [[], [], []]
for n in range(0, 3):
    for num in range(0,3):
        matriz[n].append(int(input(f'Digite um valor para [{n}][{num}]: ')))

print('-=' * 30)
for v in matriz:
    print(f'[{v[0]:^5}], [{v[1]:^5}], [{v[2]:^5}] ')