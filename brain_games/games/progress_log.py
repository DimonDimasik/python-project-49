from random import randint


min_num = 1
max_num = 50


def start():
    print('What number is missing in the progression?')


def ques_gen(min, max):
    progress_list = []
    max_step = 6
    lenght = 10
    next = randint(min, max)
    step = randint(min + 1, max_step)
    missed = randint(min, lenght)
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
