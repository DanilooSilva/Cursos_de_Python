from db import nova_conexao

sql = 'SELECT TEL, NOME FROM CONTATOS'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    for contato in cursor.fetchall():
        print('\t'.join(str(campo) for campo in contato))