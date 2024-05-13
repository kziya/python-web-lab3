from psycopg import Connection


def createOrderTable(connection: Connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        idUser INT,
        idFood INT,
        FOREIGN KEY (idUser) REFERENCES users(id),
        FOREIGN KEY (idFood) REFERENCES foods(id)
    );
""")
