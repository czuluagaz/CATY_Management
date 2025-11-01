# db_manager.py
# Path:
# Date= 2024-06-23
# version= 0.0
# Description:
# This script is used to manage the database for the application.
# It will create the database and tables if they do not exist.
# It will also provide functions to interact with the database.

# libraries
import sqlite3
from core.settings import db_path  # DATABASE_NAME,


class DBManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(db_path)  # + DATABASE_NAME
        self.cursor = self.connection.cursor()

    # Execute query
    def execute(self, query: str, params: tuple) -> None:
        self.cursor.execute(query, params)
        self.connection.commit()

    def create_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """
        )
        self.connection.commit()

    def add_user(self, username: str, password: str) -> None:
        self.cursor.execute(
            """
            INSERT INTO users (username, password) VALUES (?, ?)
        """,
            (username, password),
        )
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute(
            """
            SELECT * FROM users WHERE username = ?
        """,
            (username,),
        )
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
