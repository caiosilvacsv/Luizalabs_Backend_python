import sqlite3

# Caminho raiz
from pathlib import Path
ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'clientes.db')
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

#Criando uma tabela
def criar_tabela(connect, cursor):
  cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
  connect.commit()
  
#Inserindo dados na tabela
def inserir_dados(connect, cursor, nome, email):
  data = (nome, email)
  cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
  #Comitando as alterações - modo de como fazer multiplas transações no banco
  connect.commit()

#Atualizando registros
def atualizar_registro(connect, cursor, nome, email, id):
  data = (nome, email, id)
  cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
  connect.commit()
 
#Excluindo registros
def excluir_registro(connect, cursor, id):
  data = (id,)
  cursor.execute("DELETE FROM clientes WHERE id = ?", data)
  connect.commit()

#Inserindo varios registros
def inserir_varios(connect, cursor, dados):
  cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
  connect.commit()
  
#Consulta dos registros
def consultar_registro_cliente(cursor, id):
  cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
  resultado = cursor.fetchone()
  return resultado  

#Consulta de todos os registros
def consultar_registro_clientes(cursor):
  return cursor.execute("SELECT * FROM clientes ORDER BY nome")

criar_tabela(conn, cursor) 
inserir_dados(conn, cursor, "Luizinho", "luizinho@gmail.com")
inserir_dados(conn, cursor, "teste", "teste@gmail.com")
atualizar_registro(conn, cursor, "Testinho", "testinho@gmail.com", 1)
excluir_registro(conn, cursor, 2)

dados = [
  ("Luizinho", "luizinho@gmail.com"),
  ("Testinho", "testinho@gmail.com"),
  ("testando", "testando@gmail.com")
]

inserir_varios(conn, cursor, dados)
cliente = consultar_registro_cliente(cursor, 1)
clientes = consultar_registro_clientes(cursor)

print(dict(cliente))
print(f"O meu nome é {cliente['nome']}")

print(clientes)

for cliente in clientes:
  print(dict(cliente))
