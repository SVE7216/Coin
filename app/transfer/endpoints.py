from fastapi import APIRouter, Depends
from pydantic.typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from sqlalchemy import select, insert
from app.auth.auth_config import fastapi_users
from app.auth.models import user
from app.transfer.models import type_transfer, transfer
from app.transfer.schemas import TypeCreate, TransferCreate, TypeResponce


router = APIRouter()

# Роутеры для спраочника стран
@router.post('/createTypeTranfer')
async def add_countries(name: TypeCreate, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(fastapi_users.current_user(active=True, superuser=True))):
    """Создание типа транзакции"""
    stmt = insert(type_transfer).values(**name.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post('/getTypeTransfer', response_model=List[TypeResponce])
async def add_countries(session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(fastapi_users.current_user(active=True, superuser=True))):
    """Получение типа транзакции. Только для администраторов"""
    query = select(type_transfer)
    result = await session.execute(query)
    return result.all()

# @router.post('/createTransfer')
# async def create_transfer(data: TransferCreate, session: AsyncSession = Depends(get_async_session),
#                           users: user = Depends(fastapi_users.current_user(active=True, superuser=True))):
#     stmt = insert(transfer).values(**data.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}
