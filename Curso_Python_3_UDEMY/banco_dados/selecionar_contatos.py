from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'SELECT * FROM CONTATOS'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:3d} - {contato[0]:20s} Telefone: {contato[1]}')