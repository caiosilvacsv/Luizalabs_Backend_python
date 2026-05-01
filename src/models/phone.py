
import sqlalchemy as sa
from src.database.connection import metadata

phones = sa.Table(
  "phone",
  metadata,
  sa.Column("id", sa.Integer(), primary_key=True),
  sa.Column("ddi", sa.String(3), nullable = False),
  sa.Column("ddd", sa.String(3), nullable = False),
  sa.Column("number", sa.String(9), nullable = False),
  sa.Column(
    "individual_id", 
    sa.Integer(), 
    sa.ForeignKey("individual.id", ondelete="CASCADE"), 
    nullable = False,
  ),
)