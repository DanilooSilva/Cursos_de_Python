"""
2- Crie um função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada. Façã a função1 executar
duas funções que recebam um número diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def falar_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(falar_oi, 'Luiz')
print(executando)
executando2 = mestre(saudacao, 'Luiz', saudacao="Bom dia")
print(executando2)