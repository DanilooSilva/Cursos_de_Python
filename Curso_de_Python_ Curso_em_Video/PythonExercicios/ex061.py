print('-=-' * 30)
termo = int(input('Termo: '))
razao = int(input('Razao '))
c = 1
while c <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    c += 1
print('Fim')
