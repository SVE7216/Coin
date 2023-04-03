from fastapi import APIRouter
# from starlette.responses import JSONResponse
# from app.error import ErrorHTTP


router = APIRouter()

@router.get('/getReport')
def get_report():
    """получение отчета"""
    return True
