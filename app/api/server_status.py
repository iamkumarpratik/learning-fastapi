from fastapi import APIRouter

router = APIRouter()


@router.get('/server/check_status')
async def home():
    return {'status': 'Success', 'data': 'Server is running.'}
