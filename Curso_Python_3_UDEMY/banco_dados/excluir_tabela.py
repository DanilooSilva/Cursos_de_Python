from db import nova_conexao
from mysql.connector import ProgrammingError

delete_tabela_emals = """
    DROP TABLE EMAILS
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(delete_tabela_emals)
    except ProgrammingError as e:
        print(f'Error:  {e.msg}')
    else:
        print('Comando executado com sucesso!')