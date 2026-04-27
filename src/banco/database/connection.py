"""
  Arquivo de configuração do banco de dados
"""
import databases
import sqlalchemy as sa
from src.banco.core.config import settings

#Define a URL de conexão com o banco de dados
DATABASE_URL = "sqlite:///./banco.db"

#Cria uma instância do motor de banco de dados
database = databases.Database(DATABASE_URL)
#Metodo para criar as tabelas
metadata = sa.MetaData()

if settings.ENVORINMENT == "PRODUCTION":
  engine = sa.create_engine(
    DATABASE_URL,
  )
else:
  # Motor síncrono do SQLAlchemy, usado para criar e gerenciar a estrutura das tabelas
  #'check_same_thread': False é obrigatório no SQLite para funcionar bem com o sistema assíncrono do FastAPI
  engine = sa.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
  )

