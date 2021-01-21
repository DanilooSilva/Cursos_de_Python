from collections import defaultdict
from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = '''
    SELECT  A.NOME AS NOME,  
            B.DESCRICAO AS GRUPO
    FROM    CONTATOS A
            INNER JOIN GRUPOS B ON A.IDGRUPO = B.ID
    ORDER BY B.DESCRICAO, A.NOME
'''

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['GRUPO']].append(contato['NOME'])
        print(agrupados)