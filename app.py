import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.modules.authentication.dependencies import (
    get_authentication_service, get_create_access_token_use_case)
from src.modules.authentication.dependencies_stubs import (
    get_authentication_service_stub, get_create_access_token_use_case_stub)
from src.modules.authentication.exceptions.authentication_errors import (
    InvalidAccessTokenError, InvalidCredentialsError)
from src.modules.authentication.presentation.routes.router import \
    authentication_router
from src.modules.users.dependencies import (get_create_user_use_case,
                                            get_delete_by_id_use_case,
                                            get_find_by_username_use_case,
                                            get_list_users_use_case,
                                            get_update_user_use_case,
                                            get_user_repository,
                                            get_user_unit_of_work)
from src.modules.users.dependencies_stubs import (
    get_create_user_use_case_stub, get_delete_by_id_use_case_stub,
    get_find_by_username_use_case_stub, get_list_users_use_case_stub,
    get_update_user_use_case_stub, get_user_repository_stub,
    get_user_unit_of_work_stub)
from src.modules.users.exceptions.user_errors import (UserAlreadyExistsError,
                                                      UserDoesNotExistError)
from src.modules.users.presentation.routes.router import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(authentication_router)


# users module dependencies
app.dependency_overrides[get_user_unit_of_work_stub] = get_user_unit_of_work
app.dependency_overrides[get_user_repository_stub] = get_user_repository
app.dependency_overrides[get_create_user_use_case_stub] = get_create_user_use_case
app.dependency_overrides[get_list_users_use_case_stub] = get_list_users_use_case
app.dependency_overrides[get_find_by_username_use_case_stub] = get_find_by_username_use_case
app.dependency_overrides[get_update_user_use_case_stub] = get_update_user_use_case
app.dependency_overrides[get_delete_by_id_use_case_stub] = get_delete_by_id_use_case


# authentication module dependencies
app.dependency_overrides[get_create_access_token_use_case_stub] = get_create_access_token_use_case
app.dependency_overrides[get_authentication_service_stub] = get_authentication_service


@app.exception_handler(InvalidCredentialsError)
def invalid_credentials_error_handler(_: ..., exc: InvalidCredentialsError):
    return JSONResponse(
        status_code=401,
        content={'message': exc.message}
    )


@app.exception_handler(InvalidAccessTokenError)
def invalid_access_token_error_handler(_: ..., exc: InvalidAccessTokenError):
    return JSONResponse(
        status_code=401,
        content={'message': exc.message}
    )


@app.exception_handler(UserAlreadyExistsError)
def user_already_exists_error_handler(_: ..., exc: UserAlreadyExistsError):
    return JSONResponse(
        status_code=409,
        content={'message': exc.message}
    )


@app.exception_handler(UserDoesNotExistError)
def user_does_not_exist_error_handler(_: ..., exc: UserDoesNotExistError):
    return JSONResponse(
        status_code=404,
        content={'message': exc.message}
    )


@app.get(
    '/ping',
    description='Test availability of the service'
)
async def index():
    return {'response': 'pong'}


if __name__ == '__main__':
    uvicorn.run(app)
