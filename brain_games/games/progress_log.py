from random import randint


min_num = 1
max_num = 50
amount_ques = 3


def prog_ques_gen(min, max, amount):
    i = 1
    progress_list = []
    max_step = 6
    lenght = 10

    while i <= amount:
        next = randint(min, max)
        step = randint(min + 1, max_step)
        missed = randint(min, lenght)
        numbers = ''
        index = 1

        while index <= lenght:
            if index == missed:
                numbers = numbers + '..' + ' '
                answer = str(next)
            else:
                numbers = numbers + str(next) + ' '
            next = next + step
            index += 1

        progress_list.append(numbers)
        progress_list.append(answer)
        i += 1

    return progress_list
