import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapter.rest.handlers import router as answers_router

app = FastAPI(
    title='Email answer',
    version='0.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    answers_router,
    prefix='/api/v1',
)


def main():
    uvicorn.run(
        'main:app',  # если main.py в корне модуля
        host='0.0.0.0',
        port=8000,
        reload=True,
    )


if __name__ == '__main__':
    main()
