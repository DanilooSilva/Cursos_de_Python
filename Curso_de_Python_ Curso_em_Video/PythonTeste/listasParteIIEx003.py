matriz = [[], [], []]
for c in range(0, 3):
    for n in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {n}] ')))

for v in matriz:
    print(f'[ {v[0]} ] [ {v[1]} ] [ {v[2]} ]')