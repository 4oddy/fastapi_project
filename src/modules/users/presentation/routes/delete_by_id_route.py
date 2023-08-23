from fastapi import Depends

from ...application.delete_by_id.dto import DeleteUserByIdCommand
from ...application.delete_by_id.use_case import DeleteUserByIdUseCase
from ...dependencies import get_delete_by_id_use_case
from . import router


@router.delete('/')
def delete_by_id(
        data: DeleteUserByIdCommand,
        use_case: DeleteUserByIdUseCase = Depends(get_delete_by_id_use_case)
):
    result = use_case(data)
    return result
