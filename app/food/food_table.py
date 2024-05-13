from psycopg import Connection


def createFoodTable(connection: Connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS foods (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL,
        price FLOAT
    );
    """)
