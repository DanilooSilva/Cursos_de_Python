from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = '''
    SELECT  A.NOME, 
            A.TEL, 
            B.DESCRICAO 
    FROM    CONTATOS A
            INNER JOIN GRUPOS B ON A.IDGRUPO = B.ID
    ORDER BY B.DESCRICAO, A.NOME
'''

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'Nome: {contato[0]:10s} tel: {contato[1]:15s} grupo: {contato[2]}')