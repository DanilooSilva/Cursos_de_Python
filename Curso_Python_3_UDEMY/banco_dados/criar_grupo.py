from mysql.connector.errors import ProgrammingError
from db import nova_conexao

tabela_grupo = """
    CREATE TABLE IF NOT EXISTS GRUPOS(
        ID INT AUTO_INCREMENT PRIMARY KEY,
        DESCRICAO VARCHAR(30)
    )
"""

alterar_tabela_contato_addcampo = """
    ALTER TABLE CONTATOS ADD COLUMN IDGRUPO INT
"""

alterar_tabela_contato = """
    ALTER TABLE CONTATOS ADD FOREIGN KEY (IDGRUPO)
    REFERENCES GRUPOS (ID)
"""


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_grupo)
        cursor.execute(alterar_tabela_contato_addcampo)
        cursor.execute(alterar_tabela_contato)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Tabela(s) alterada(s) com sucesso!')