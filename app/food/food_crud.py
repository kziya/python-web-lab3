from bson import ObjectId
from fastapi import HTTPException
from pymongo.database import Database

from .food_schemas import Food


def get_food_by_name(db: Database, name: str) -> Food:
    collection = db['users']

    doc = dict(collection.find_one({'name': name}))

    return Food(name=doc['name'], price=doc['price'], id=str(doc['_id']))


def created_food(db: Database, name: str, price: float) -> Food:
    collection = db['users']

    insertRes = collection.insert_one({'name': name, 'price': price})

    return get_food_by_id(db, str(insertRes.inserted_id))


def get_food_by_id(db: Database, food_id: str) -> Food:
    collection = db['users']

    doc = collection.find_one({'_id': ObjectId(food_id)})

    if doc is None:
        raise HTTPException(status_code=404, detail="Food not found")

    return Food(name=doc['name'], price=doc['price'], id=str(food_id))


def updated_food(db: Database, id: str, name: str, price: float) -> Food:
    collection = db['users']
    updateObject = {}
    if name is not None:
        updateObject['name'] = name
    if price is not None:
        updateObject['price'] = price

    collection.update_one({'_id': ObjectId(id)}, {'$set': updateObject})
    return get_food_by_id(db, id)


def delete_food(db: Database, food_id: str) -> None:
    db['users'].delete_one({'_id': ObjectId(food_id)})
    return None
