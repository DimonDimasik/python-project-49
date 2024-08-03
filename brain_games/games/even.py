from random import randint


MIN = 1
MAX = 100
START = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def question_answer():
    question = randint(MIN, MAX)
    if is_even(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
