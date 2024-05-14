from random import randint
from brain_games.cli import welcome_user
from .game_logic import question_answer, is_win


max_num = 100
min_num = 1
amount_ques = 3


def gcd_greeting():
    print('Find the greatest common divisor of given numbers.')


def gcd_ques_gen(max, min, amount):
    num_list = []
    i = 1
    while i <= amount * 2:
        num_list.append(randint(min, max))
        i += 1

    ques_list = []
    i = 0

    while i <= amount * 2 - 2:
        question = f'{num_list[i]} {num_list[i + 1]}'

        if num_list[i] == num_list[i + 1]:
            answer = num_list[i]

        elif num_list[i] > num_list[i + 1]:
            for item in range(num_list[i], 0, -1):
                if num_list[i] % item == 0 and num_list[i + 1] % item == 0:
                    answer = item
                    break

        elif num_list[i] < num_list[i + 1]:
            for item in range(num_list[i + 1], 0, -1):
                if num_list[i] % item == 0 and num_list[i + 1] % item == 0:
                    answer = item
                    break

        ques_list.append(question)
        ques_list.append(str(answer))
        i += 2

    return ques_list


def brain_gcd():
    user_name = welcome_user()
    gcd_greeting()
    ques_answ_list = gcd_ques_gen(max_num, min_num, amount_ques)
    check_win_list = question_answer(ques_answ_list)
    is_win(check_win_list, user_name)
