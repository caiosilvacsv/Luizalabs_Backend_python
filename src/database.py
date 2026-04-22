import os
import databases
import sqlalchemy as sa

# Define a string de conexão para um banco de dados SQLite local
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

# Instância assíncrona do banco, usada para as operações (CRUD) nas rotas
database = databases.Database(DATABASE_URL)

# Motor síncrono do SQLAlchemy, usado para criar e gerenciar a estrutura das tabelas
# 'check_same_thread': False é obrigatório no SQLite para funcionar bem com o sistema assíncrono do FastAPI
engine = sa.create_engine(
  DATABASE_URL, 
  connect_args = {"check_same_thread" : False}
  )
metadata = sa.MetaData()
