cont = mult = 0
while True:
    print('-=-' * 30)
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    print('-=-' * 30)
    cont = 0
    if tabu < 0:
        break
    while cont <= 10:
        mult = tabu * cont
        print(f'{tabu} x {cont} = {mult}')
        cont += 1
print('Programa Tabuada Encerrado. Volte Sempre !')