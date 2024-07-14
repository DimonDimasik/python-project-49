from random import randint


MIN = 1
MAX = 100


def start():
    print('Find the greatest common divisor of given numbers.')


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def question_answer():
    first_num = randint(MIN, MAX)
    second_num = randint(MIN, MAX)
    question = f'{first_num} {second_num}'
    answer = str(gcd(first_num, second_num))
    return question, answer
