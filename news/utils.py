import random


def generate_random_string(number):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ""
    for i in range(number):
        string += random.choice(chars)
    return string