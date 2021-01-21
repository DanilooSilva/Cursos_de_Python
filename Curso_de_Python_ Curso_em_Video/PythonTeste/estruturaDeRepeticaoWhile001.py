'''cont = 1
while cont < 10:
    print(cont)
    cont += 1'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))