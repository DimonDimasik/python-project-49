from random import randint


max_num = 100
min_num = 1


def start():
    print('Find the greatest common divisor of given numbers.')


def ques_gen(min, max):
    first_num = randint(min, max)
    second_num = randint(min, max)

    ques_list = []

    question = f'{first_num} {second_num}'

    if first_num == second_num:
        answer = first_num

    elif first_num > second_num:
        for item in range(second_num, 0, -1):
            if first_num % item == 0 and second_num % item == 0:
                answer = item
                break

    elif first_num < second_num:
        for item in range(first_num, 0, -1):
            if first_num % item == 0 and second_num % item == 0:
                answer = item
                break

    ques_list.append(question)
    ques_list.append(str(answer))

    return ques_list
