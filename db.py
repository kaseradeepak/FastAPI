# pip3 install sqlalchemy
# SQL Databases - SQLite / MySQL / PostrgeSQL / OracleDB / MSSQL
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./sqlite.db"
engine = create_engine(DATABASE_URL, echo=True)