from db import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS CONTATOS (NOME VARCHAR(50), TEL VARCHAR(40))
"""

tabela_emails = """
    CREATE TABLE EMAILS(
        ID INT AUTO_INCREMENT PRIMARY KEY,
        DONO VARCHAR(50)
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')