import sqlite3

conn = sqlite3.connect(
    "../database/customer_platform.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users"
)

users = cursor.fetchall()

for user in users:
    print(user)

conn.close()