from mysql.connector import ProgrammingError
from db import nova_conexao

alterar_tabela = """
    ALTER TABLE CONTATOS ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(alterar_tabela)
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
    else:
        print('Executado com Sucesso!')