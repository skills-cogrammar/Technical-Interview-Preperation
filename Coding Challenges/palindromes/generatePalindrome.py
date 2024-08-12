import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_palindrome(length):
    half = generate_random_string(length // 2)
    return half + half[::-1]


def getWordList():
    return [
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100),
    generate_palindrome(100),
    generate_random_string(100)
        ]