import sqlite3

# Caminho raiz
from pathlib import Path
ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'clientes.db')
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Digite o id do cliente: ")

#Consulta de todos os registros de forma incorreta
clientes = cursor.execute(f"SELECT * FROM clientes WHERE id = {id_cliente}").fetchall()

for cliente in clientes:
  print(dict(cliente))