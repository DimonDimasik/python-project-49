from random import randint
from brain_games.cli import welcome_user
from .game_logic import question_answer, is_win


min_num = 1
max_num = 100
amount_ques = 3


def even_greeting():
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


def brain_even():
    user_name = welcome_user()
    even_greeting()
    ques_answ_list = even_ques_gen(min_num, max_num, amount_ques)
    check_win_list = question_answer(ques_answ_list)
    is_win(check_win_list, user_name)
