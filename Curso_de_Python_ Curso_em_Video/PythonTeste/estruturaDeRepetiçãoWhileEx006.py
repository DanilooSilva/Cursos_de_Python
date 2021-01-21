cont = 1
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = 0
qnt = 10
while decimo != qnt:
    print(termo, end=' ')
    termo += razao
    decimo += 1

while cont != 0:
    novotermo = int(input('\nDeseja mostrar mais quantos termos: '))
    qnt += novotermo
    if novotermo != 0:
        while decimo != qnt:
            print(termo, end=' ')
            termo += razao
            decimo += 1
    else:
        cont = novotermo
print('Acabou')