class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_user(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")


if __name__ == "__main__":

    user1 = User(
        username="deva",
        email="deva@gmail.com"
    )

    user1.display_user()