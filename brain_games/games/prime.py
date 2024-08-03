from random import randint
import math


MIN = 1
MAX = 100
START = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Checks if a number is prime
    Keyword argument:
    number: int
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def question_answer():
    """
    Returns a random number and the answer
    to the question whether the number is prime
    """
    question = randint(MIN, MAX)
    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
