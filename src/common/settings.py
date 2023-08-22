from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Users'

    db_url: str = 'sqlite:///testdb.db'
