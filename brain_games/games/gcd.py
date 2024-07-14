from random import randint


MIN = 1
MAX = 100


def start():
    print('Find the greatest common divisor of given numbers.')


def gcd(num_1, num_2):
    while num_2:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def question_answer():
    first_num = randint(MIN, MAX)
    second_num = randint(MIN, MAX)
    question = f'{first_num} {second_num}'
    answer = str(gcd(first_num, second_num))
    return question, answer
