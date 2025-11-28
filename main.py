# main.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapter.rest.handlers import router as answers_router
from adapter.rest.settings import get_settings

settings = get_settings()

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


def main() -> None:
    uvicorn.run(
        'main:app',
        host=settings.host,
        port=settings.port,
        reload=settings.dev,
    )


if __name__ == '__main__':
    main()
