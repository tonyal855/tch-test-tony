import random
import string

def random_digit_string(length=15):
    return ''.join(random.choices(string.digits, k=length))

