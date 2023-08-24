from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from . import router

from ...dependencies import get_authentication_service, AuthenticationService
from ...application.create_access_token.dto import CreateAccessTokenCommand


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.post('/')
def create_access_token(
    data: CreateAccessTokenCommand,
    auth_service: AuthenticationService = Depends(get_authentication_service)
):
    user = auth_service.authenticate_user(data.username, data.password)
    token = auth_service.create_access_token(
        {'sub': user.username}
    )
    return {'token': token, 'type': 'bearer'}
