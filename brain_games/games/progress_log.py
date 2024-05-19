from random import randint
from brain_games.cli import welcome_user
from .game_logic import question_answer, is_win


min_num = 1
max_num = 50
amount_ques = 3


def progress_start():
    print('What number is missing in the progression?')


def prog_ques_gen(min, max, amount):
    i = 1
    progress_list = []
    max_step = 6
    lenght = 10

    while i <= amount:
        next = randint(min, max)
        step = randint(min + 1, max_step)
        missed = randint(min, lenght)
        numbers = ''
        index = 1

        while index <= lenght:
            if index == missed:
                numbers = numbers + '..' + ' '
                answer = str(next)
            else:
                numbers = numbers + str(next) + ' '
            next = next + step
            index += 1

        progress_list.append(numbers)
        progress_list.append(answer)
        i += 1

    return progress_list


def brain_progress():
    user_name = welcome_user()
    progress_start()
    ques_answ_list = prog_ques_gen(min_num, max_num, amount_ques)
    check_win_list = question_answer(ques_answ_list)
    is_win(check_win_list, user_name)
