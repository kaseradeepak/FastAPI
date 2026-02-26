# Create Tables.
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

# id, name, email, .... 
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String(50), nullable=False, unique=True),
    Column("address", String(100), nullable=False),
    Column("phone_number", Integer, nullable=False)
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("content", String(500), nullable=False)
)

def create_tables():
    metadata.create_all(engine)