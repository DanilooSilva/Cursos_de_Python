from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA funcao {funcao.__name__} '
              f'levou {tempo:.2f}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(12):
        print(i, end='')



demora()