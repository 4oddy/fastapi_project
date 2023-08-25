from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ...application.create_access_token.dto import CreateAccessTokenCommand
from ...application.create_access_token.use_case import \
    CreateAccessTokenUseCase
from ...dependencies_stubs import get_create_access_token_use_case_stub
from . import router

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.post('/')
def create_access_token(
    data: CreateAccessTokenCommand,
    use_case: CreateAccessTokenUseCase = Depends(get_create_access_token_use_case_stub)
):
    token = use_case(data)
    return {'token': token, 'type': 'bearer'}
