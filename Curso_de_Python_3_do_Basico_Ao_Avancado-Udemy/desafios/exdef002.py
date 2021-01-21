"""
2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""


def isfloat(valor):
    try:
        float(valor)
    except ValueError:
        return False
    return True


numeros = []
cont = 1
while True:
    n = input(f'Digite {cont} número: ')

    if isfloat(n):
        numeros.append(float(n))
    else:
        print(f'{n} não é um número')
        continue
    cont += 1
    if len(numeros) == 3:
        break


def soma(numero1=0, numero2=0, numero3=0):
    print(f'A soma dos números: {numero1} + {numero2} + {numero3} = {numero1 + numero2 + numero3}')


print(soma(numeros[0], numeros[1], numeros[2]))