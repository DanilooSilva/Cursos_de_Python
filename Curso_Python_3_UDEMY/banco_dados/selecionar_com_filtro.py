from db import nova_conexao

sql = 'SELECT * FROM CONTATOS WHERE TEL = "94955-2951"'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)