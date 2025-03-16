import random
import string


def generate_random_credentials():
    letters = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()-_=+"

    username_length = random.randint(6, 10)
    username = ''.join(random.choice(letters + digits) for _ in range(username_length))

    domain = "freepass.ai"

    email = f"{username}@{domain}"

    password_chars = [
        random.choice(letters),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    remaining_length = 12 - len(password_chars)
    all_chars = letters + string.ascii_uppercase + digits + special_chars
    password_chars.extend(random.choice(all_chars) for _ in range(remaining_length))

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    return (email, password)
