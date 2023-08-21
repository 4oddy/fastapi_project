from fastapi import Depends

from ...application.create_user.dto import CreateUserCommand
from ...application.create_user.use_case import CreateUserUseCase
from ...dependencies import get_create_user_usecase


from fastapi import APIRouter


router = APIRouter(
    tags=['users'],
)


@router.post('/create/')
def create_user(
        data: CreateUserCommand,
        use_case: CreateUserUseCase = Depends(get_create_user_usecase)
):
    user = use_case(data)
    return user
