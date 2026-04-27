import sqlalchemy as sa
from src.banco.database.connection import metadata

clients = sa.Table(
  "client",
  metadata,
  sa.Column("id",     sa.Integer(), primary_key = True),
  sa.Column("name",   sa.String, nullable = False),
  sa.Column(
    "created_at",
    sa.TIMESTAMP(timezone=True),
    server_default = sa.func.now(),
    nullable = False
  ),
  sa.Column("status", sa.Boolean, default = False),
  sa.Column("closed", sa.TIMESTAMP(timezone=True), nullable = True),
)