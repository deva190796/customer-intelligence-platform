import sqlite3

from config import DATABASE_PATH


def create_database():
    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                    )
                """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    prediction INTEGER,
    result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

    conn.commit()

    conn.close()

    print("Database Created Successfully")


if __name__ == "__main__":
    create_database()