import random
import string

def get_random_string(length):
    # With combination of lower and upper case
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def generate_password_with_special_characters(lenght):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(lenght))
    # Output $z#m;-fb
    # Approach second
    #return ''.join(random.choice(string.printable) for i in range(lenght))
