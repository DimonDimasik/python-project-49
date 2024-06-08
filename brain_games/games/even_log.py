from random import randint


min_num = 1
max_num = 100


def start():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def ques_gen(min, max):
    question = randint(min, max)
    ques_list = []
    ques_list.append(question)
    if question % 2 == 0:
        answer = 'yes'
        ques_list.append(answer)
    else:
        answer = 'no'
        ques_list.append(answer)

    return ques_list
