from fastapi.routing import APIRouter


router = APIRouter(
    prefix='/token',
    tags=['token']
)
