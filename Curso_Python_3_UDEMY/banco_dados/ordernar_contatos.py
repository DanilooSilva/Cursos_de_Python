from db import nova_conexao

sql = 'SELECT NOME FROM CONTATOS ORDER BY NOME'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(registro[0] for registro in cursor))