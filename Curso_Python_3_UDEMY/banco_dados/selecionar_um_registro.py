from db import nova_conexao

sql = 'SELECT TEL, NOME FROM CONTATOS LIMIT 2 OFFSET 0'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    print(cursor.fetchone())
    print(cursor.fetchone())        