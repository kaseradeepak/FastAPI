from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from db_orm import orm_engine

class Base(DeclarativeBase):
    pass # Placeholder - Do Nothing! 

# Double Underscore = __ 
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

# class Post(Base):
#     __tablename__ = "posts"

def create_tables():
    Base.metadata.create_all(orm_engine)