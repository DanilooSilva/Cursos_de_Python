from mysql.connector.errors import ProgrammingError
from db import nova_conexao

selecionar_grupo = 'SELECT ID FROM GRUPOS WHERE DESCRICAO = %s'
atualizar_contato = 'UPDATE CONTATOS SET IDGRUPO = %s WHERE NOME = %s'

contato_grupo = {
    'Allanys':'Trabalho',
    'Danilo':'Casa',
    'Maria':'Casa',
    'Mel':'Trabalho',
    'Ohara':'Casa',
    'Scarlett':'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            idgrupo = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (idgrupo, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos Associados')