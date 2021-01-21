from mysql.connector import ProgrammingError
from db import nova_conexao

seleciona_tabelas = """
    SHOW TABLES
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(seleciona_tabelas)

        for n, table in enumerate(cursor, start=1):
            print(f'{n}ª Tabela: {table[0]}')
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
    else:
        print('Executado Com Sucesso!')