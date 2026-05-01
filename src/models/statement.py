
import sqlalchemy as sa
from src.database.connection import metadata

type_transaction = sa.Enum(
  'DEPOSIT',
  'WITHDRAWAL',
  'TRANSFER',
  name='type_transaction'
)

statements = sa.Table(
  "statement",
  metadata,
  sa.Column("id", sa.Integer(), primary_key=True),
  sa.Column("amount", sa.DECIMAL(precision = 10, scale = 2), nullable = False),
  sa.Column("type_transaction", type_transaction, nullable = False),
  sa.Column("description", sa.String(150), nullable = False),
  sa.Column(
    "created_at",
    sa.TIMESTAMP(timezone=True),
    server_default = sa.func.now(),
    nullable = False
  ),
  sa.Column(
    "account_id", 
    sa.Integer(), 
    sa.ForeignKey("account.id", ondelete="CASCADE"), 
    nullable = False,
  ),
)