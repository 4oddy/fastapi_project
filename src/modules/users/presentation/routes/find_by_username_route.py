from fastapi import Depends

from ...application.find_by_username.dto import FindByUsernameQuery
from ...application.find_by_username.use_case import FindByUsernameUseCase
from ...dependencies_stubs import get_find_by_username_use_case_stub
from . import router


@router.get('/{username}')
def find_by_username(
        username: str,
        use_case: FindByUsernameUseCase = Depends(get_find_by_username_use_case_stub)
):
    query = FindByUsernameQuery(username=username)
    return use_case(query)
