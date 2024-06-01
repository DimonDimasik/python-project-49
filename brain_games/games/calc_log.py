from random import randint


min_num = 1
max_num = 15
amount_ques = 3


def calc_ques_gen(min, max, amount):
    num_list = []
    i = 1
    while i <= amount * 2:
        num_list.append(randint(min, max))
        i += 1

    i = 0
    quest_list = []

    while i <= 4:
        action = randint(1, 3)

        if action == 1:
            question = f'{num_list[i]} + {num_list[i + 1]}'
            answer = str(num_list[i] + num_list[i + 1])
            quest_list.append(question)
            quest_list.append(answer)

        elif action == 2:
            question = f'{num_list[i]} - {num_list[i + 1]}'
            answer = str(num_list[i] - num_list[i + 1])
            quest_list.append(question)
            quest_list.append(answer)

        elif action == 3:
            question = f'{num_list[i]} * {num_list[i + 1]}'
            answer = str(num_list[i] * num_list[i + 1])
            quest_list.append(question)
            quest_list.append(answer)

        i += 2
    return quest_list
