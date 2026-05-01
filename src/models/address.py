
import sqlalchemy as sa 
from src.database.connection import metadata


address = sa.Table(
  "address",
  metadata,
  sa.Column("id", sa.Integer(), primary_key = True),
  sa.Column("postal_code", sa.String(20), nullable = False),
  sa.Column("address_line_1", sa.String(150), nullable = False),
  sa.Column("address_line_2", sa.String(10), nullable = False),
  sa.Column("district", sa.String(100), nullable = False),
  sa.Column("city", sa.String(100), nullable = False),
  sa.Column("state", sa.String(100), nullable = False),
  sa.Column("country", sa.String(100), nullable = False),
  sa.Column(
    "created_at",
    sa.TIMESTAMP(timezone=True),
    server_default = sa.func.now(),
    nullable = False
  ),
  sa.Column(
    "individual_id", 
    sa.Integer(), 
    sa.ForeignKey("individual.id", ondelete="CASCADE"), 
    nullable = False,
  ),
)