from psycopg import Connection


def createUserTable(connection: Connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255),
        password VARCHAR(255),
        role  VARCHAR(255)
    );
    """)
