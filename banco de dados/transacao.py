import sqlite3

# Caminho raiz
from pathlib import Path
ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'clientes.db')
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

#Gerenciando transações
#Usando tratamento de excepções para realizar a transação e fazer o rollback
try:
  cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Coitadinho", "coitadinho@gmail"))
  #conn.commit()  ## Caso haja algum erro no fim ele irá voltar somente o estado após este commit 
  cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)", (1, "Olokito", "olokito@gmail"))
  conn.commit()
except Exception as e:
  print(f"OPS! Ocorreu um erro: {e}")
  conn.rollback()
  