from fastapi import Depends

from . import router

from ...application.list_users.use_case import ListUsersUseCase
from ...dependencies import get_list_users_use_case


@router.get('/')
def list_users(use_case: ListUsersUseCase = Depends(get_list_users_use_case)):
    users = use_case()
    return users
