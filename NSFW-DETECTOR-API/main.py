from fastapi import FastAPI
from app import main_router

app = FastAPI()

app.include_router(main_router, prefix="/api")