while True:
    print('-' * 50)
    tabuada = int(input('Quer ver a tabuada de qual valor ? '))
    cont = mult = 0
    print('-' * 50)
    if tabuada < 0:
        break
    while cont <= 10:
        print(f'{tabuada} x {cont} = {mult}')
        cont += 1
        mult = tabuada * cont
print('O programa acabou! ')