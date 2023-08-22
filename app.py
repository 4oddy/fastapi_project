import uvicorn
from fastapi import FastAPI

from src.modules.users.presentation.routes.router import user_router

app = FastAPI()

app.include_router(user_router)


@app.get('/ping/')
async def index():
    return {'response': 'pong'}


if __name__ == '__main__':
    uvicorn.run(app)
