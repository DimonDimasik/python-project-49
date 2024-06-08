from random import randint


min_num = 2
max_num = 100


def start():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ques_gen(min, max):
    ques_list = []
    question = randint(min, max)
    if question == 2 or question == 3:
        answer = 'yes'
    else:
        half = question // 2
        for item in range(half, min - 1, -1):
            if question % item == 0:
                answer = 'no'
                break

            else:
                answer = 'yes'

    ques_list.append(question)
    ques_list.append(answer)

    return ques_list
