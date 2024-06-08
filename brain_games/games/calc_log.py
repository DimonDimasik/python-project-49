from random import randint


min_num = 1
max_num = 15


def start():
    print('What is the result of the expression?')


def ques_gen(min, max):
    num_list = []
    num_list.append(randint(min, max))
    num_list.append(randint(min, max))

    quest_list = []
    action = randint(1, 3)

    if action == 1:
        question = f'{num_list[0]} + {num_list[1]}'
        answer = str(num_list[0] + num_list[1])
        quest_list.append(question)
        quest_list.append(answer)

    elif action == 2:
        question = f'{num_list[0]} - {num_list[1]}'
        answer = str(num_list[0] - num_list[1])
        quest_list.append(question)
        quest_list.append(answer)

    elif action == 3:
        question = f'{num_list[0]} * {num_list[1]}'
        answer = str(num_list[0] * num_list[1])
        quest_list.append(question)
        quest_list.append(answer)

    return quest_list
