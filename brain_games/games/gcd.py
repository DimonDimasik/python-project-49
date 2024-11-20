from random import randint


MIN = 1
MAX = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Returns greatest common divisor"""
    while b:
        a, b = b, a % b
    return a


def generate():
    """Generates a question and the correct answer"""
    first_num = randint(MIN, MAX)
    second_num = randint(MIN, MAX)
    question = f'{first_num} {second_num}'
    answer = gcd(first_num, second_num)
    return question, answer
