from fastapi import Depends

from ...application.find_by_username.dto import FindByUsernameQuery
from ...application.find_by_username.use_case import FindByUsernameUseCase
from ...dependencies import get_find_by_username_use_case
from . import router


@router.get('/{username}')
def find_by_username(
        username: str,
        use_case: FindByUsernameUseCase = Depends(get_find_by_username_use_case)
):
    query = FindByUsernameQuery(username=username)
    return use_case(query)
