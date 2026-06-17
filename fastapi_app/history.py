import sqlite3

DATABASE_PATH = "../database/customer_platform.db"


def save_prediction(
    email,
    prediction,
    result
):

    conn = sqlite3.connect(
        DATABASE_PATH
    )

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

    conn = sqlite3.connect(
        DATABASE_PATH
    )

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