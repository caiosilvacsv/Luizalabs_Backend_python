from databases import Database
import sqlalchemy as sa

from src.core.config import settings

database = Database(settings.DATABASE_URL, min_size=5, max_size=10)
metadata = sa.MetaData()

if settings.ENVIRONMENT == "production":
    engine = sa.create_engine(settings.DATABASE_URL)
else:
    engine = sa.create_engine(settings.DATABASE_URL)
