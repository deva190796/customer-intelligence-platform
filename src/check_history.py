import sqlite3

conn = sqlite3.connect(
    "../database/customer_platform.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT *
    FROM prediction_history
    """
)

rows = cursor.fetchall()

for row in rows:

    print(row)

conn.close()