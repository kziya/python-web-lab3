from fastapi import APIRouter, Depends
from psycopg import Cursor

from app.db import get_db
from app.food import food_crud
from app.food import food_schemas

router = APIRouter()


@router.get("/food/{food_id}", response_model=food_schemas.Food)
async def get_food_by_id(food_id: int, db: Cursor = Depends(get_db)):
    return food_crud.get_food_by_id(db, food_id)


@router.post("/food", response_model=food_schemas.Food)
async def create_food(createFood: food_schemas.CreateFood, db: Cursor = Depends(get_db)):
    return food_crud.created_food(db, createFood.name, createFood.price)


@router.patch("/food/{food_id}", response_model=food_schemas.Food)
async def update_food(food_id: int, updateFood: food_schemas.UpdateFood, db: Cursor = Depends(get_db)):
    return food_crud.updated_food(db, food_id, updateFood.name, updateFood.price)


@router.delete("/food/{food_id}", response_model=None)
async def delete_food(food_id: int, db: Cursor = Depends(get_db)):
    return food_crud.delete_food(db, food_id)
