termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = 0
while decimo != 10:
    print(termo, end=' ')
    termo += razao
    decimo += 1
