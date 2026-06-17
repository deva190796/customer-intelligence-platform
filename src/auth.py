import sqlite3

from config import DATABASE_PATH


def register_user(username, email, password):

    conn = sqlite3.connect(str(DATABASE_PATH))
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users(username,email,password)
            VALUES(?,?,?)
            """,
            (username, email, password)
        )

        conn.commit()

        print("User Registered Successfully")

    except sqlite3.IntegrityError:

        print("Email already exists")

    finally:

        conn.close()


def login_user(email, password):

    conn = sqlite3.connect(str(DATABASE_PATH))

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email=? AND password=?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        print("Login Successful")
        print(user)

    else:

        print("Invalid Credentials")


if __name__ == "__main__":

    register_user(
        username="deva",
        email="deva@gmail.com",
        password="123456"
    )

    login_user(
        email="deva@gmail.com",
        password="123456"
    )