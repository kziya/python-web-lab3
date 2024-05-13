import os

import psycopg

from .food.food_table import createFoodTable
from .order.order_table import createOrderTable
from .user.user_table import createUserTable

connection = psycopg.connect(user=os.getenv("DB_USER"),
                             password=os.getenv("DB_PASSWORD"),
                             host=os.getenv('DB_HOST'),
                             port=os.getenv('DB_PORT'),
                             dbname=os.getenv('DB_NAME')
                             )


def get_db():
    return connection.cursor()


# Create tables
createFoodTable(connection)
createUserTable(connection)
createOrderTable(connection)

connection.commit()
