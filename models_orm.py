from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from db_orm import orm_engine

class Base(DeclarativeBase):
    pass # Placeholder - Do Nothing! 

# Double Underscore = __ 
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    # list[post] => Don't a create a columnn for list of posts in the DB table.
    # back_populates is used to link two ORM models bidirectionally in a relationship.
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")

# User ---- Post => 1:M
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="posts")

def create_tables():
    Base.metadata.create_all(orm_engine)