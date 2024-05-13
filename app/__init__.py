from fastapi import FastAPI

from .food import food_router

app = FastAPI()

app.include_router(food_router.router)
