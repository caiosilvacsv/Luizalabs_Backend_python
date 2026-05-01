
import sqlalchemy as sa
from src.database.connection import metadata

accounts = sa.Table(
  "account",
  metadata,
  sa.Column("id", sa.Integer(), primary_key=True),
  sa.Column("agency", sa.Integer(), nullable = False),
  sa.Column("account_number", sa.Integer(), nullable = False, unique = True ),
  sa.Column("account_digit", sa.Integer(), nullable = False),
  sa.Column("is_active", sa.Boolean, default = True, nullable = False),
  sa.Column(
    "balance", 
    sa.DECIMAL(precision = 10, scale = 2), 
    server_default = "0.00",
    nullable = False 
  ),
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
