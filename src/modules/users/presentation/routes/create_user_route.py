from fastapi import Depends

from ...application.create_user.dto import CreateUserCommand
from ...application.create_user.use_case import CreateUserUseCase
from ...dependencies import get_create_user_use_case
from . import router


@router.post('/')
def create_user(
        data: CreateUserCommand,
        use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    user = use_case(data)
    return user
