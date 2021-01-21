from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='DaniloGomes04'
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE AGENDA')