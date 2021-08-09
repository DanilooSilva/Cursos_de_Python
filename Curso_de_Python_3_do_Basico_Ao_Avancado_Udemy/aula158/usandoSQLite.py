import sqlite3

conexao = sqlite3.connect(r'aula158\basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nm_cliente TEXT,'
#                'vl_peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nm_cliente, vl_peso) VALUES (?, ?)', ('Maria', 50))
# cursor.execute(
#     'INSERT INTO clientes (nm_cliente, vl_peso) VALUES (:nome, :peso)', 
#     {'nome':'Ohara', 'peso':18}
# )
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)', 
#     {'id': None, 'nome':'Ohara', 'peso':18}
# )
# conexao.commit()

cursor.execute('UPDATE clientes SET nm_cliente=:nome WHERE id_cliente=:id', {'id':'4', 'nome':'Allanys'})
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    ident, nome, peso = linha
    print(ident, nome, peso)

cursor.close()
conexao.close()
