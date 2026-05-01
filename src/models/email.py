
import sqlalchemy as sa
from src.database.connection import metadata

emails = sa.Table(
  "email",
  metadata,
  sa.Column("id", sa.Integer(), primary_key=True),
  sa.Column("email", sa.String, nullable = False),
  sa.Column(
    "individual_id", 
    sa.Integer(), 
    sa.ForeignKey("individual.id", ondelete="CASCADE"), 
    nullable = False,
  ),
)