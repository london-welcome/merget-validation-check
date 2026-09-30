class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


def fetch_user(user_id):
    users = {
        1: User(1, "Alice", "alice@example.com"),
        2: User(2, "Bob", "bob@example.com"),
    }

    return users.get(user_id)


def format_user(user):
    if not user:
        return "User not found"

    return f"{user.name} <{user.email}>"


def print_user(user_id):
    user = fetch_user(user_id)
    print(format_user(user))