"""
1 - Crie um função que receba uma funcao2 como parâmetro e retorne o valor da função2 executada.
"""


def ola_mundo():
    return 'Olá mundo!'


def mestre(funcao):
    return funcao()


executando = mestre(ola_mundo)
print(executando)
