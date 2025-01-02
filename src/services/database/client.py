import sqlite3
from typing import Optional, List, Dict, Union
from config.logger import logger


class DatabaseManager:
    def __init__(self, db_path: str = "users.db"):
        self.connection: Optional[sqlite3.Connection] = None
        self.db_path = db_path

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            logger.log(20, "Successfully connected to the SQLite database!")
        except Exception as e:
            logger.log(50, "Error connecting to SQLite: ", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            logger.log(20, "Connection to SQLite closed!")

    def execute(
        self,
        query: str,
        args: tuple = (),
        fetch: bool = False,
        fetchone: bool = False,
        execute: bool = False,
    ) -> Union[List[Dict], Dict, None]:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)

            if fetch:
                return [dict(row) for row in cursor.fetchall()]
            elif fetchone:
                row = cursor.fetchone()
                return dict(row) if row else None
            elif execute:
                self.connection.commit()
                return None
        except sqlite3.Error as e:
            logger.log(40, f"SQLite error: {e}")
            return None

    def create_table(self):
        """Creates the `users` table if it doesn't exist."""
        query = """
        CREATE TABLE users (
            telegram_id BIGINT PRIMARY KEY,
            fullname VARCHAR(255),
            username VARCHAR(255),
            referrer_id BIGINT,
            is_completed BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.execute(query, execute=True)

    def create_user(self, telegram_id: int, fullname: str, username: str, referrer_id: str):
        query_user = """
        INSERT INTO users (telegram_id, fullname, username, referrer_id)
        VALUES (?, ?, ?, ?);
        """
        self.execute(
            query_user,
            (telegram_id, fullname, username, referrer_id),
            execute=True
        )

    def get_user(self, telegram_id: int) -> Optional[Dict]:
        query_user = "SELECT * FROM users WHERE telegram_id = ?;"
        return self.execute(query_user, (telegram_id,), fetchone=True)

    def get_users_count_by_referrer(self, referrer_id: int) -> int:
        query_users = "SELECT COUNT(*) AS count FROM users WHERE referrer_id = ?;"
        result = self.execute(query_users, (referrer_id,), fetchone=True)
        return result["count"] if result else 0

    def update_user_completed(self, telegram_id: int):
        query = "UPDATE users SET is_completed = 1 WHERE telegram_id = ?;"
        self.execute(query, (telegram_id,), execute=True)

    def get_users_count(self) -> int:
        query = "SELECT COUNT(*) AS count FROM users;"
        result = self.execute(query, fetchone=True)
        return result["count"] if result else 0

    def get_completed_users_count(self) -> int:
        query = "SELECT COUNT(*) AS count FROM users WHERE is_completed = 1;"
        result = self.execute(query, fetchone=True)
        return result["count"] if result else 0

    def get_all_users(self) -> List[Dict]:
        query = "SELECT * FROM users;"
        return self.execute(query, fetch=True)