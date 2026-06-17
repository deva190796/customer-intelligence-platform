import sqlite3

from pydantic import BaseModel

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.security import hash_password
from src.security import verify_password

DATABASE_PATH = "../database/customer_platform.db"


class UserRegister(BaseModel):

    username: str
    email: str
    password: str


def register_user(user: UserRegister):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (username,email,password)
            VALUES (?,?,?)
            """,
            (
                user.username,
                user.email,
                hash_password(user.password)
            )
        )

        conn.commit()

        return {
            "message":
            "User Registered Successfully"
        }

    except Exception as e:

        return {
            "error":
            str(e)
        }

    finally:

        conn.close()
def login_user(email, password):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE email=?
        """,
        (email,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:

        return {
            "message": "Invalid Credentials"
        }

    stored_password = row[0]

    if verify_password(
        password,
        stored_password
    ):

        return {
            "message": "Login Successful",
            "email": email
        }

    return {
        "message": "Invalid Credentials"
    }
class UserLogin(BaseModel):

    email: str
    password: str