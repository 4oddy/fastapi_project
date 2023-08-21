import uvicorn
from fastapi import FastAPI

from src.modules.users.presentation.routes.create_user_route import router

app = FastAPI()

app.include_router(router)


@app.get('/ping/')
async def index():
    return {'response': 'pong'}


if __name__ == '__main__':
    uvicorn.run(app)
