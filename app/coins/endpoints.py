from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from pydantic.typing import List
from app.auth.auth_config import fastapi_users
from app.database import get_async_session
from sqlalchemy import select, insert, delete, update
from app.coins.models import countries, currency, origin_of_coin, type_coin, collections, coins
from app.coins.schemas import GuideCreate, GuideResponse, CoinsCreate, CollectionResponce, CoinsRepsonse
from app.auth.models import user
from app.logger_config import logger



router = APIRouter()


# получение активного пользователя
current_user = fastapi_users.current_user(active=True)

# получение активного и с меткой супер пользователя
current_superuser = fastapi_users.current_user(active=True, superuser=True)

# Роутеры для справочника стран
@router.post('/createCountries')
async def add_countries(name: GuideCreate, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(current_superuser)):
    """Создание новой страны в спровочнике. Страна уникальная. Доступно только администратору"""
    try:
        stmt = insert(countries).values(**name.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.patch('/updateCountries')
async def update_countries(countries_id: int, name: str, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(current_superuser)):
    """Обновление название страны в спровочнике. Доступно только администратору"""
    try:
        update_stmt = (update(countries).where(countries.c.id==countries_id)\
                       .values(name=name))
        await session.execute(update_stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.delete('/deleteCountries')
async def del_countries(countries_id: int, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(current_superuser)):
    """Удаление страны из спраочника по id. Дотсупно только администратору"""
    try:
        stmt = delete(countries).where(countries.c.id == countries_id)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


@router.get('/getCountries', response_model=List[GuideResponse])
async def get_countriess(session: AsyncSession = Depends(get_async_session),
                         users: user = Depends(current_user)):
    """Получение всех стран из справочника. Дотсупна всем пользователям, которые вошли в систему"""
    try:
        query = select(countries)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


# Роутеры для справочника валюты
@router.post('/createCurrency')
async def add_currency(name: GuideCreate, session: AsyncSession = Depends(get_async_session),
                       users: user = Depends(current_superuser)):
    """Создание новой валюты в спровочнике. Валюта уникальная. Доступно только администратору"""
    try:
        stmt = insert(currency).values(**name.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.patch('/updateCurrency')
async def update_currency(currency_id: int, name: str, session: AsyncSession = Depends(get_async_session),
                       users: user = Depends(current_superuser)):
    """Обновление названия валюты. Доступно только администратору"""
    try:
        update_stmt = (update(currency).where(currency.c.id==currency_id)\
                       .values(name=name))
        await session.execute(update_stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.delete('/deleteCurrency')
async def del_currency(currency_id: int, session: AsyncSession = Depends(get_async_session),
                       users: user = Depends(current_superuser)):
    """Удаление валюты в справочнике по id, доступно только администратору"""
    try:
        stmt = delete(currency).where(currency.c.id == currency_id)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


@router.get('/getCurrency', response_model=List[GuideResponse])
async def get_currency(session: AsyncSession = Depends(get_async_session),
                       users: user = Depends(current_user)):
    """Получение всех валют, дотсупно всем пользователям вошедшим в систему"""
    try:
        query = select(currency)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


# Роутеры для справочника происхождения(монетный двор)
@router.post('/createOriginOfCoin')
async def add_origin_of_coin(name: GuideCreate, session: AsyncSession = Depends(get_async_session),
                             users: user = Depends(current_superuser)):
    """
    Создание новоого места происхождения(монетного двора) в спровочнике. Название уникальное.
    Доступно только администратору
    """
    try:
        stmt = insert(origin_of_coin).values(**name.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.patch('/updateOriginOfCoin')
async def update_origin_of_coin(origin_of_coin_id: int, name: str, session: AsyncSession = Depends(get_async_session),
                             users: user = Depends(current_superuser)):
    """Обовление именини монетного двора. Дотсупно только администратору"""
    try:
        update_stmt = (update(origin_of_coin).where(origin_of_coin.c.id==origin_of_coin_id)\
                       .values(name=name))
        await session.execute(update_stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


@router.delete('/deleteOriginOfCoin')
async def del_origin_of_coin(origin_of_coin_id: int, session: AsyncSession = Depends(get_async_session),
                             users: user = Depends(current_superuser)):
    """Удаление монетного двора по id. Доступно только администратору"""
    try:
        stmt = delete(origin_of_coin).where(origin_of_coin.c.id == origin_of_coin_id)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.get('/getOriginOfCoin', response_model=List[GuideResponse])
async def get_origin_of_coin(session: AsyncSession = Depends(get_async_session),
                             users: user = Depends(current_superuser)):
    """Полуяение списка монетных дворов. Доступно всем пользователям вошедшим в систему"""
    try:
        query = select(origin_of_coin)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


# Роутеры для справочника типа монеты
@router.post('/createTypeCoin')
async def add_type_coin(name: GuideCreate, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(fastapi_users.current_user(active=True, superuser=True))):
    """Создание нового типа монеты в спровочнике. Тип монеты уникальный. Дотсупно только администратору"""
    try:
        stmt = insert(type_coin).values(**name.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.patch('/updateTypeCoin')
async def update_type_coin(type_coin_id: int, name: str, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(fastapi_users.current_user(active=True, superuser=True))):
    """Обновление имени типа монеты. Дотсупно только администратору"""
    try:
        update_stmt = (update(type_coin).where(type_coin.c.id==type_coin_id)\
                       .values(name=name))
        await session.execute(update_stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.delete('/deleteTypeCoin')
async def del_type_coin(type_coin_id: int, session: AsyncSession = Depends(get_async_session),
                        users: user = Depends(fastapi_users.current_user(active=True, superuser=True))):
    """Удаление типы монеты по id. Доступно только администратору"""
    try:
        stmt = delete(type_coin).where(type_coin.c.id == type_coin_id)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


@router.get('/getTypeCoin', response_model=List[GuideResponse])
async def get_countries(session: AsyncSession = Depends(get_async_session), users: user = Depends(current_user)):
    """Получение данных из спраочника. Доступно только пользователям вошедшим в систему"""
    try:
        query = select(type_coin)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


# Роутеры для коллекций

@router.post('/createCollection')
async def create_collection(name: str, description: str, users: user = Depends(current_user),
                            session: AsyncSession = Depends(get_async_session)):
    """Создание новой коллеции. Коллекция автоматически привязывается к пользователю, который делает запрос"""
    try:
        stmt = insert(collections).values({'name': name, 'description': description, 'user_id': users.id})
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.delete('/deleteCollection')
async def del_collection(collection_id: int, users: user = Depends(current_superuser),
                            session: AsyncSession = Depends(get_async_session)):
    """Удаление коллекции по id. Дотсупно только администратору"""
    try:
        stmt = delete(collections).where(collections.c.id == collection_id)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.patch('/updateCollection')
async def update_collection(collection_id: int, name: str, description: str, users: user = Depends(current_superuser),
                            session: AsyncSession = Depends(get_async_session)):
    """изменение данных коллекции по id. Дотсупно только администратору"""
    try:
        update_stmt = (update(collections).where(collections.c.id == collection_id)\
                       .values(name=name, description=description))
        await session.execute(update_stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.get('/getCollection', response_model=List[CollectionResponce])
async def get_сollection(session: AsyncSession = Depends(get_async_session), users: user = Depends(current_superuser)):
    """Получение всех коллекций хранящихся в бд. Доступно только для администратора"""
    try:
        query = select(collections)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.get('/getCollectionUser', response_model=List[CollectionResponce])
async def get_сollection_user(users: user = Depends(fastapi_users.current_user(active=True)),
                              session: AsyncSession = Depends(get_async_session)):
    """Получение списка коллекций, по id пользователя, который делает запрос"""
    try:
        query = select(collections).where(collections.c.user_id==users.id)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


# Роутеры для занесения монет
@router.post('/createCoin')
async def create_coin(data: CoinsCreate, session: AsyncSession = Depends(get_async_session)):
    """Создание монеты"""
    try:
        stmt = insert(coins).values(**data.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)


@router.get('/getCoinsAdmin', response_model=List[CoinsRepsonse])
async def get_сoins(session: AsyncSession = Depends(get_async_session),
                    users: user = Depends(current_superuser)):
    """Получение всех монет. Только для администратора"""
    try:
        query = select(coins.c.id, coins.c.name, coins.c.description, coins.c.collections_id, collections.c.name,
                           coins.c.nominal_value, coins.c.currency_id, currency.c.name, coins.c.year,
                       coins.c.is_existence,coins.c.serial_number, coins.c.type_coin_id, type_coin.c.name,
                       coins.c.origin_of_coin_id, origin_of_coin.c.name,coins.c.countries_id, countries.c.name,
                       coins.c.created_at
                       ).join(currency, coins.c.currency_id == currency.c.id)\
            .join(collections, coins.c.collections_id==collections.c.id)\
            .join(type_coin, coins.c.type_coin_id==type_coin.c.id)\
            .join(origin_of_coin, coins.c.origin_of_coin_id==origin_of_coin.c.id)\
            .join(countries, coins.c.countries_id == countries.c.id)

        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень  coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.get('/getCoinsUser', response_model=List[CoinsRepsonse])
async def get_сoins_user(users: user = Depends(fastapi_users.current_user(active=True)),
                         session: AsyncSession = Depends(get_async_session)):
    """получение только активных монет запрашиваемоего пользователя"""
    try:
        query = select(user.c.username, user.c.id, coins.c.id, coins.c.name, coins.c.description,
                       coins.c.collections_id, collections.c.name,
                           coins.c.nominal_value, coins.c.currency_id, currency.c.name, coins.c.year,
                       coins.c.is_existence,
                           coins.c.serial_number, coins.c.type_coin_id, type_coin.c.name, coins.c.origin_of_coin_id,
                       origin_of_coin.c.name,coins.c.countries_id, countries.c.name, coins.c.created_at
                       ).join(currency, coins.c.currency_id == currency.c.id)\
            .join(collections, coins.c.collections_id==collections.c.id)\
            .join(type_coin, coins.c.type_coin_id==type_coin.c.id)\
            .join(origin_of_coin, coins.c.origin_of_coin_id==origin_of_coin.c.id)\
            .join(countries, coins.c.countries_id == countries.c.id) \
            .join(user, collections.c.user_id == user.c.id).where(user.c.id==users.id).where(coins.c.is_existence==True)

        result = await session.execute(query)
        return result.all()
    except Exception as error:
        logger.error(f"Ошибка. Уровень  coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)

@router.patch('updateStatusCoins')
async def update_coins(coins_id:int,name: str, description: str, is_existence: bool,
                 users: user = Depends(fastapi_users.current_user(active=True)),
                         session: AsyncSession = Depends(get_async_session)):
    """Обновление информации по монете"""
    try:
        update_stmt = (update(coins).where(coins.c.id == coins_id)\
                       .values(
            name=name, description=description, is_existence=is_existence
            )
        )
        await session.execute(update_stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        logger.error(f"Ошибка. Уровень coins --- {error}")
        return JSONResponse(content={'status': False, 'error': error}, status_code=500)
