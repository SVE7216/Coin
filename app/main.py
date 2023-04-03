from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.auth.auth_config import auth_backend, fastapi_users
from app.auth.schemas import UserRead, UserCreate

app = FastAPI(title='Coins')
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

current_superuser = fastapi_users.current_user(active=True, superuser=True)

@app.get('/api/system/status')
def get_system_status():
    """проверки роботособности системы. Возвращает {'status': True}, если сервис нах. в раб. сост."""
    return {'status': True}

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


def configurate_routers():
    from app.coins.endpoints import router as coins_router
    from app.report.endpoints import router as report_router
    from app.transfer.endpoints import router as transfer_router

    app.include_router(coins_router, prefix='/api/coins', tags=['Coins'])
    app.include_router(transfer_router, prefix='/api/transfer', tags=['Transfer'])
    app.include_router(report_router, prefix='/api/report', tags=['Report'])


configurate_routers()
