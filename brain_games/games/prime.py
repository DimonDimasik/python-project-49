from random import randint


MIN = 2
MAX = 100


def start():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    if number == 2 or number == 3:
        return True
    else:
        half = number // 2
        for item in range(MIN, half + 1):
            if number % item == 0:
                return False
        return True


def question_answer():
    question = randint(MIN, MAX)
    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
