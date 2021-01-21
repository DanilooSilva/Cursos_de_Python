from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO CONTATOS (NOME, TEL) VALUES (%s, %s)'
args = (
    ('Danilo','94955-2951'),
    ('Maria','97757-0961'),
    ('Allanys','96659-5697'),
    ('Scarlett','94122-2526'),
    ('Ohara','93345-5556'),
    ('Mel','95525-3011'),
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros inclídos')
        