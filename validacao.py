import mysql # type: ignore
from usuario import Usuario

Conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12102021',
    database='aulas'
)

cursor = Conexao.cursor()

## CRUD

cursor.close()
Conexao.close()
