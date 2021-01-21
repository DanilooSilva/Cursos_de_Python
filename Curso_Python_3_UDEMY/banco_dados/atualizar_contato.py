from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'UPDATE CONTATOS SET TEL = %s WHERE NOME = %s'
args = ('3599-2921', 'Ohara',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizado(s).')