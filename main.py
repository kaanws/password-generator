import random
import string


def generate_password():

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(digits),
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(special_characters)
    ]

    remaining_chars = random.choices(string.ascii_letters + string.digits + string.punctuation, k=4)
    password += remaining_chars

    random.shuffle(password)

    return ''.join(password)


print(generate_password())
