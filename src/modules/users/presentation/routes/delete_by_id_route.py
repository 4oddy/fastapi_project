from fastapi import Depends

from ...application.delete_by_id.use_case import DeleteUserByIdUseCase
from ...dependencies import get_delete_by_id_use_case
from . import router


@router.delete('/{user_id}')
def delete_by_id(
        user_id: str,
        use_case: DeleteUserByIdUseCase = Depends(get_delete_by_id_use_case)
):
    result = use_case(user_id)
    return result
