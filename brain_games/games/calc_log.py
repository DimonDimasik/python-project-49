from random import randint
from brain_games.cli import welcome_user
from .game_logic import question_answer, is_win


min_num = 1
max_num = 15
amount_ques = 3


def calc_greeting():
    print('What is the result of the expression?')


def calculate_ques_gen(min, max, amount):
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


def brain_calc():
    user_name = welcome_user()
    calc_greeting()
    ques_answ_list = calculate_ques_gen(min_num, max_num, amount_ques)
    check_win_list = question_answer(ques_answ_list)
    is_win(check_win_list, user_name)
