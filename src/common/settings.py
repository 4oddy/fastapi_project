from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Users and their wishes'

    db_url: str = 'sqlite:///metanit2.db'
