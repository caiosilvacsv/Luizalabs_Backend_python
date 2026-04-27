
import sqlalchemy as sa
from src.banco.database.connection import metadata

current_accounts = sa.Table(
  "current_account",
  metadata,
  sa.Column("id", sa.Integer(), primary_key=True),
  sa.Column(
    "daily_limit",
    sa.DECIMAL(precision = 10, scale = 2),
    server_default = "200.00",
    nullable = False
  ),
  sa.Column(
    "daily_withdrawal", 
    sa.Integer(),
    server_default = "3",
    nullable = False
  ),
  sa.Column(
    "account_id", 
    sa.Integer(), 
    sa.ForeignKey("account.id", ondelete="CASCADE"), 
    nullable = False,
  ),
)