numero = int(input('Digite um número de 0 a 9999 '))
if  numero >= 0 and numero <= 9999:
    numero = str(numero)
    print('Unidade {}'.format(numero[3]))
    print('Dezena {}'.format(numero[2]))
    print('Centena {}'.format(numero[1]))
    print('Milhar {}'.format(numero[0]))
else:
    print('Atenção numero de 0 a 9999')
