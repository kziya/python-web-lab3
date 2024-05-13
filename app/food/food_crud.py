from fastapi import HTTPException
from psycopg import Cursor

from .food_schemas import Food


def get_food_by_name(cursor: Cursor, name: str) -> Food:
    result = cursor.execute("SELECT * FROM foods WHERE name = %s", (name,)).fetchone()
    print(result)

    return result


def created_food(cursor: Cursor, name: str, price: float) -> Food:
    cursor.execute("INSERT INTO foods (name, price) VALUES (%s, %s) RETURNING id, name, price;", (name, price,))
    result = cursor.fetchone()

    cursor.connection.commit()
    food = Food(id=result[0], name=result[1], price=result[2])
    return food


def get_food_by_id(cursor: Cursor, food_id: int) -> Food:
    result = cursor.execute("SELECT * FROM foods WHERE id = %s", (food_id,)).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Food not found")

    return Food(id=result[0], name=result[1], price=result[2])


def updated_food(cursor: Cursor, id: int, name: str, price: float) -> Food:
    queryString = "UPDATE foods SET"
    parameters = []

    if name is not None:
        # Check if the new name already exists
        isExistsName = get_food_by_name(cursor, name)
        if isExistsName is not None:
            raise HTTPException(status_code=400, detail="Food name already exists")
        queryString += " name = %s"
        parameters.append(name)

    if price is not None:
        if name is not None:
            queryString += ","
        queryString += " price = %s"
        parameters.append(price)

    queryString += " WHERE id = %s RETURNING id, name, price;"
    parameters.append(id)

    cursor.execute(queryString, parameters)

    updated_row = cursor.fetchone()
    cursor.connection.commit()

    return Food(id=updated_row[0], name=updated_row[1], price=updated_row[2])


def delete_food(cursor: Cursor, food_id: int) -> None:
    isExists = get_food_by_id(cursor, food_id);
    if isExists is None:
        raise HTTPException(status_code=404, detail="Food not found")

    cursor.execute("DELETE FROM foods WHERE id = %s", (food_id,))
    cursor.connection.commit()
    return None
