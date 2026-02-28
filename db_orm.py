# This file creates a Session for SQLAlchemy ORM.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sqlite.db"

orm_engine = create_engine(DATABASE_URL, echo=True)
orm_session = sessionmaker(bind=orm_engine)

# ORM -> Object Relation Mapping.
# User Model -> User table