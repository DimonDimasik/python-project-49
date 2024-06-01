from random import randint


min_num = 1
max_num = 100
amount_ques = 3


def even_start():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_ques_gen(min, max, amount):
    num_list = []
    i = 1
    while i <= amount:
        num_list.append(randint(min, max))
        i += 1

    ques_list = []
    i = 0

    while i <= amount - 1:
        question = num_list[i]
        ques_list.append(question)
        if question % 2 == 0:
            answer = 'yes'
            ques_list.append(answer)
        else:
            answer = 'no'
            ques_list.append(answer)
        i += 1
    return ques_list
