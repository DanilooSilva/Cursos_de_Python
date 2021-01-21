from db import nova_conexao

sql = "SELECT * FROM CONTATOS WHERE NOME LIKE '%a%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)