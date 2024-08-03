from random import randint


MIN = 1
MAX = 50
START = 'What number is missing in the progression?'


def progression():
    """
    Returns an arithmetic progression of
    10 numbers in increments from 2 to 7
    """
    lenght = 10
    numbers = []
    step = randint(2, 7)
    next = randint(MIN, MAX)
    i = 1
    while i <= lenght:
        numbers.append(next)
        next += step
        i += 1
    return numbers


def question_answer():
    """
    Removes a randomly selected number from
    an arithmetic progression and returns the
    progression and the removed number
    """
    missed = randint(0, 9)
    num_list = progression()
    answer = str(num_list[missed])
    num_list[missed] = '..'
    new_list = []
    for i in num_list:
        new_list.append(str(i))
    question = ' '.join(new_list)
    return question, answer
