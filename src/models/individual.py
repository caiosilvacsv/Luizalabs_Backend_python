import sqlalchemy as sa
from src.database.connection import metadata

#Criando uma tabela com sqlalchemy
individuals = sa.Table(
  "individual",
  metadata,
  sa.Column("id", sa.Integer(), primary_key=True),
  sa.Column("cpf", sa.String(11), unique = True, nullable = False),
  sa.Column("date_of_birth", sa.Date()),
  sa.Column(
    "created_at",
    sa.TIMESTAMP(timezone=True),
    server_default = sa.func.now(),
    nullable = False
  ),
  sa.Column(
    "client_id", 
    sa.Integer(), 
    sa.ForeignKey("client.id", ondelete="CASCADE"), 
    nullable = False,
  ),
)