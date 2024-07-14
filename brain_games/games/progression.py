from random import randint


MIN = 1
MAX = 50


def start():
    print('What number is missing in the progression?')


def question_answer():
    progress_list = []
    max_step = 6
    lenght = 10
    next = randint(MIN, MAX)
    step = randint(MIN + 1, max_step)
    missed = randint(MIN, lenght)
    numbers = ''
    i = 1

    while i <= lenght:
        if i == missed:
            numbers = numbers + '..' + ' '
            answer = str(next)
        else:
            numbers = numbers + str(next) + ' '
        next = next + step
        i += 1

    progress_list.append(numbers)
    progress_list.append(answer)

    return progress_list
