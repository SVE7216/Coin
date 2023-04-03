import datetime
from pydantic import BaseModel

class GuideCreate(BaseModel):
    """Схема для создания спраочника"""
    name: str

class GuideResponse(BaseModel):
    """Схема для создания спраочника"""
    id: int
    name: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class CollectionCreate(BaseModel):
    """Схема для создания коллекций"""
    name: str
    description: str

    class Config:
        orm_mode = True

class CoinsCreate(BaseModel):
    name: str
    description: str
    collections_id: int
    nominal_value: str
    currency_id: int
    year: str
    serial_number: str
    type_coin_id: int
    origin_of_coin_id: int
    countries_id: int


class CollectionResponce(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class CoinsRepsonse(BaseModel):
    username: str
    user_id: int
    id: int
    name: str
    description: str
    collections_id: int
    collections_name: str
    nominal_value: str
    currency_id: int
    currency_name: str
    year: str
    is_existence: bool
    serial_number: str
    type_coin_id: int
    type_coin_name: str
    origin_of_coin_id: int
    origin_of_coin_name: str
    countries_id: int
    countries_id: str
    created_at: datetime.datetime


    class Config:
        orm_mode = True