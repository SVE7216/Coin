from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, BOOLEAN
from app.auth.models import user
from datetime import datetime


metadata = MetaData()

#Таблица справочник стран
countries = Table(
    'countries',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)

# Таблица справочник валют
currency = Table(
    'currency',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)

#тип монеты
type_coin = Table(
    'type_coin',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())

)

# Справочник происхождению монет
origin_of_coin = Table(
    'origin_of_coin',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)

collections = Table(
    'collections',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('description', String, nullable=True),
    Column('user_id', Integer, ForeignKey(user.c.id), nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)

coins = Table(
    'coins',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('description', String, nullable=True),
    Column('collections_id', Integer, ForeignKey(collections.c.id), nullable=False),
    Column('nominal_value', String, nullable=False),
    Column('currency_id', Integer, ForeignKey(currency.c.id), nullable=False),
    Column('year', String, nullable=False),
    Column('is_existence', BOOLEAN, nullable=True, default=True),
    Column('serial_number', String, nullable=False),
    Column('type_coin_id', Integer, ForeignKey(type_coin.c.id), nullable=False),
    Column('origin_of_coin_id', Integer, ForeignKey(origin_of_coin.c.id), nullable=False),
    Column('countries_id', Integer, ForeignKey(countries.c.id), nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow())
)
