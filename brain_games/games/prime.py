from random import randint


MIN = 2
MAX = 100


def start():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question_answer():
    ques_list = []
    question = randint(MIN, MAX)
    if question == 2 or question == 3:
        answer = 'yes'
    else:
        half = question // 2
        for item in range(half, MIN - 1, -1):
            if question % item == 0:
                answer = 'no'
                break

            else:
                answer = 'yes'

    ques_list.append(question)
    ques_list.append(answer)

    return ques_list
