from typing import Optional

from pydantic import BaseModel


class Food(BaseModel):
    id: str
    name: str
    price: float


class CreateFood(BaseModel):
    name: str
    price: float


class UpdateFood(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
