# This class contains method on Strings
import string
import random

def generate_random_string_lowercase(length):
    value=''.join(random.choices(string.ascii_lowercase, k = int(length)))
    print('Generated String Is : '+value)
    return value

def generate_random_string_alphanumeric(length):
    value=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k = int(length)))
    print('Generated String Is : '+value)
    return value

def generate_random_special_char(length):
    special_char = ['@', '#', '$', '%', '*', '&']
    value=''.join(random.choices(special_char, k = length))
    print('Generated Special Character String Is : '+value)
    return value

def generate_random_string_uppercase(length):
    value=''.join(random.choices(string.ascii_uppercase, k = int(length)))
    print('Generated String Is : '+value)
    return value




