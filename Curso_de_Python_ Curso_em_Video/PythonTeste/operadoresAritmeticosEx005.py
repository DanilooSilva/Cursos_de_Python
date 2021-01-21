n = int(input('Digite um numero: '))
cont = 0
i = 0
result = 0
while cont < 11:
    result = n * cont
    print('{} x {} = {}'. format(n, cont, result))
    cont += 1
