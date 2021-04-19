import random
import string


def get_random_string(length):
    # With combination of lower and upper case
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def get_simple_password(length):
    return f'aA@1{get_random_string(length)}'


def generate_password_with_special_characters(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(length))
