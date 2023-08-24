from datetime import timedelta

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Users'
    secret_key: str = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

    db_url: str = 'sqlite:///testdb.db'

    expires_delta_access_token: timedelta = timedelta(minutes=15)
