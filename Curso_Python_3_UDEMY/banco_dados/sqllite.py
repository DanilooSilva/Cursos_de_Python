from sqlite3 import connect, ProgrammingError, Row

tabela_grupo = '''CREATE TABLE IF NOT EXISTS GRUPOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DESCRICAO VARCHAR(30)

)'''

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS CONTATOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME VARCHAR(50), 
        TEL VARCHAR(40),
        IDGRUPO INTEGER,
        FOREIGN KEY (IDGRUPO) REFERENCES GRUPOS (ID)
    )
"""

insert_gurpos = 'INSERT INTO GRUPOS (DESCRICAO) VALUES (?)'
select_grupos = 'SELECT ID, DESCRICAO FROM GRUPOS'
insert_contatos = 'INSERT INTO CONTATOS (NOME, TEL, IDGRUPO) VALUES (?, ?, ?)'
select = """
    SELECT  B.DESCRICAO AS GRUPO, A.NOME AS CONTATO
    FROM    CONTATOS A
            INNER JOIN GRUPOS B ON A.IDGRUPO = B.ID
    ORDER BY GRUPO, CONTATO
"""

try:
    conexao = connect(':memory:')
    conexao.row_factory = Row
    cursor = conexao.cursor()

    cursor.execute(tabela_grupo)
    cursor.execute(tabela_contatos)

    cursor.executemany(insert_gurpos, (('Casa',), ('Trabalho',)))
    cursor.execute(select_grupos)
    grupos = {row['DESCRICAO']: row['ID'] for row in cursor.fetchall()}

    contatos = (
        ('Danilo', 124, grupos['Casa']),
        ('Maria', 352, grupos['Casa']),
        ('Scarlett', 557, grupos['Trabalho']),
        ('Allanys', 785, None),
        ('Mel', 879, None),
        ('Ohara', 597, None),
    )

    cursor.executemany(insert_contatos, contatos)

    cursor.execute(select)
    for contato in cursor:
        print(contato['CONTATO'], contato['GRUPO'])
except ProgrammingError as e:
    print(f'Erro: {e.msg}')