from fastapi import Depends

from . import router

from ...dependencies import get_find_by_username_use_case

from ...application.find_by_username.dto import FindByUsernameQuery


@router.get('/{username}')
def find_by_username(username, use_case=Depends(get_find_by_username_use_case)):
    query = FindByUsernameQuery(username=username)
    return use_case(query)
