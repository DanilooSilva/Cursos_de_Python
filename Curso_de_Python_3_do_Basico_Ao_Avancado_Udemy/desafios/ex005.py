"""
   Faça um lista de tarefas com as seguintes opções:
        adicionar tarefa
        listar tarefas
        opção de desfazer (a cada vez que chamarmos, desfaz a útima ação)
        opção de refazer (a cada vez que chamarmos, refaz a última ação) 

        ['Tarefa 1', 'Tarefa 2']
        ['Tarefa 1'] <- Desfazer
        ['Tarefa 1', 'Tarefa 2'] < - Refazer
"""

from time import sleep

def add_tarefas(tarefa, lista):
    lista.append(tarefa)


def listar_tarefas(lista):
    for tarefa in lista:
        print(tarefa)
        sleep(3)


def desfazer(lista, lista_bkp):
    lista.pop()
    lista_bkp.append()



lista_tarefas = []
lista_tarefas_bkp = []
tarefa = ''


while True:
    print('*-*' * 30)
    print('''Selecione uma Opção: 
        1 - Adicionar uma Tarefa
        2 - Listar tarefas
        3 - Desfazer
        4 - Refazer
        0 - Sair
    ''')
    print('*-*' * 30)
    opcao = input('Digite aqui: ')
    sleep(3)
    if int(opcao) == 0:
        break
    elif int(opcao) == 1:
        tarefa = str(input('Digite a Tarefa: '))
        add_tarefas(tarefa, lista_tarefas)
        print('Tarefa adicionada.')
    elif int(opcao) == 2:
        listar_tarefas(lista_tarefas)
    elif int(opcao) == 3:
        desfazer(lista_tarefas)
    elif int(opcao) == 4:
        add_tarefas(lista_tarefas_bkp[-1], lista_tarefas)
    else:
        print('Opção Inválida')

