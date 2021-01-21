s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        print(c)
print('A soma de todos os valore divissiveis por 3 de 1, 500 é {}'.format(s))