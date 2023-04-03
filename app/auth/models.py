from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, BOOLEAN
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from app.database import Base

metadata = MetaData()

# таблица возможных ролей пользователя
user_role = Table(
    'user_role',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name_role', String, nullable=False, unique=True),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)

# Таблица пользователей
user = Table(
    "user",
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", BOOLEAN, default=True, nullable=False),
    Column("is_superuser", BOOLEAN, default=False, nullable=False),
    Column("is_verified", BOOLEAN, default=False, nullable=False),
    Column('role_id', Integer, ForeignKey(user_role.c.id), nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(BOOLEAN, default=True, nullable=False)
    is_superuser: bool = Column(BOOLEAN, default=False, nullable=False)
    is_verified: bool = Column(BOOLEAN, default=False, nullable=False)
    role_id = Column(Integer, ForeignKey(user_role.c.id))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
