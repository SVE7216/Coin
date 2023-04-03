import datetime

from pydantic import BaseModel

class TypeCreate(BaseModel):
    """Схема для создания типа трансфера"""
    name: str

    class Config:
        orm_mode = True


class TypeResponce(BaseModel):
    """Схема для возврата пользователя типа транзакции"""
    id: int
    name: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class TransferCreate(BaseModel):
    seller_id: int
    coin_id: int
    buyer_id: int
    price: int
    type_transfer_id: int
