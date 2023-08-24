import uvicorn
from fastapi import FastAPI

from src.modules.users.presentation.routes.router import user_router
from src.modules.authentication.presentation.routes.router import authentication_router

app = FastAPI()

app.include_router(user_router)
app.include_router(authentication_router)


@app.get('/ping/')
async def index():
    return {'response': 'pong'}


if __name__ == '__main__':
    uvicorn.run(app)
