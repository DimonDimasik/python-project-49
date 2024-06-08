from random import randint


max_num = 100
min_num = 1


def start():
    print('Find the greatest common divisor of given numbers.')


def ques_gen(min, max):
    num_list = []
    num_list.append(randint(min, max))
    num_list.append(randint(min, max))

    ques_list = []

    question = f'{num_list[0]} {num_list[1]}'

    if num_list[0] == num_list[1]:
        answer = num_list[0]

    elif num_list[0] > num_list[1]:
        for item in range(num_list[1], 0, -1):
            if num_list[0] % item == 0 and num_list[1] % item == 0:
                answer = item
                break

    elif num_list[0] < num_list[1]:
        for item in range(num_list[0], 0, -1):
            if num_list[0] % item == 0 and num_list[1] % item == 0:
                answer = item
                break

    ques_list.append(question)
    ques_list.append(str(answer))

    return ques_list
