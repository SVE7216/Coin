from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, BOOLEAN
from sqlalchemy.orm import DeclarativeBase
from app.auth.models import user
from datetime import datetime
from app.coins.models import coins



metadata = MetaData()

type_transfer = Table(
    'type_transfer',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)

transfer = Table(
    'transfer',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('seller_id', ForeignKey(user.c.id), nullable=False),
    Column('coin_id', ForeignKey(coins.c.id), nullable=False),
    Column('buyer_id', ForeignKey(user.c.id), nullable=False),
    Column('price', Integer, nullable=False),
    Column('type_transfer_id', ForeignKey(type_transfer.c.id), nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)
