from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "customer_platform.db"


def save_prediction(email, prediction, result):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history
        (
            email,
            prediction,
            result
        )
        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            email,
            prediction,
            result
        )
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM prediction_history
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows