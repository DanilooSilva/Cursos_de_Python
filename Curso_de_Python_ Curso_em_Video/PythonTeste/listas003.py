a = [2, 3, 4, 7]
b = a #ligação entre listas a e b
c = b[:] #copia da lista b
c[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')