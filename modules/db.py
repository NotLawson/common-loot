# Database module
# This module contains the Database class to handle to the postgres database.
import psycopg2


class Database:
    def __init__(self, dbname, user, password, host, port, init_tables=True):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.init_tables()

    def init_tables(self):
        # Initialize the database tables if they do not exist.
        
        # Orders Table
        # This table stores the orders made by users.
        # - id: Unique identifier for each order
        # - link: A unique link to the order, used for tracking.
        # - items: The items in the order. This is an array of product IDs.
        # - quantity: The quantity of items in the order. This is an array of integers.
        # - total_price: The total price of the order.
        # - created_at: The timestamp of when the order was created.
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                link VARCHAR(255) NOT NULL UNIQUE,
                items INTEGER[] NOT NULL,
                quantity INTEGER[] NOT NULL,
                total_price DECIMAL(10, 2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

    def execute_query(self, query, params=()):
        # Execute a query on the database
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    def execute_command(self, command, params=()):
        # Execute a command on the database
        self.cursor.execute(command, params)
