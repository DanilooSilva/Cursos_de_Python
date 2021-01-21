n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Numero: '))
    if n != 999:
        cont += 1
        soma += n
    else:
        n = 999
print('Foram digitados {} números e a soma deles é {}'.format(cont, soma))