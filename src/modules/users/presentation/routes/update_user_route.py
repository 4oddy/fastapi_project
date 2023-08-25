from fastapi import Depends

from ...application.update_user.dto import UpdateUserCommand
from ...application.update_user.use_case import UpdateUserUseCaseImpl
from ...dependencies_stubs import get_update_user_use_case_stub
from . import router


@router.put('/{user_id}')
def update_user(
        user_id: str,
        data: UpdateUserCommand,
        use_case: UpdateUserUseCaseImpl = Depends(get_update_user_use_case_stub)
):
    res = use_case((user_id, data))
    return res
