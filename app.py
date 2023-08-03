from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get('/ping/')
async def index():
    return {'response': 'pong'}


if __name__ == '__main__':
    uvicorn.run(app)
