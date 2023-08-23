from fastapi import Depends

from ...application.update_user.dto import UpdateUserCommand
from ...dependencies import get_update_user_use_case
from . import router


@router.put('/')
def update_user(
        data: UpdateUserCommand,
        use_case = Depends(get_update_user_use_case)
):
    res = use_case(data)
    return res
