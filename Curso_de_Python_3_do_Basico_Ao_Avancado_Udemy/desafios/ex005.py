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


def desfazer(lista, lista_bkp):
    if not lista:
        print('Nada a desfazer')
        return

    valor_bkp = lista.pop()
    lista_bkp.append(valor_bkp)


def refazer(lista, lista_bkp):
    if not lista:
        print('Nada a refazer')
        return

    valor_bkp = lista_bkp.pop()
    lista.append(valor_bkp)


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
    if int(opcao) == 0:
        break
    elif int(opcao) == 1:
        tarefa = str(input('Digite a Tarefa: '))
        add_tarefas(tarefa, lista_tarefas)
        print('Tarefa adicionada.')
    elif int(opcao) == 2:
        listar_tarefas(lista_tarefas)
    elif int(opcao) == 3:
        desfazer(lista_tarefas, lista_tarefas_bkp)
    elif int(opcao) == 4:
        refazer(lista_tarefas, lista_tarefas_bkp)
    else:
        print('Opção Inválida')

