"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o
valor do primeiro número somado do aumento do percentual do mesmo.
"""


def aumento(valor=0, aumento=0):
    return valor + (valor * aumento) / 100


print(f'{aumento(50, 22):.2f}')