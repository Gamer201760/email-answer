import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapter.rest.handlers import router as answers_router

load_dotenv()

DEV = bool(os.getenv('DEV', 'True'))

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
        'main:app',
        host=os.getenv('HOST', 'localhost'),
        port=int(os.getenv('PORT', '8000')),
        reload=DEV,
    )


if __name__ == '__main__':
    main()
