from random import randint
from brain_games.cli import welcome_user
from .game_logic import question_answer, is_win


min_num = 2
max_num = 100
amount_ques = 3


def prime_start():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime_ques_gen(min, max, amount):
    i = 1
    num_list = []
    while i <= amount:
        num_list.append(randint(min, max))
        i += 1

    i = 0
    ques_list = []
    while i < amount:
        if num_list[i] == 2 or num_list[i] == 3:
            question = num_list[i]
            answer = 'yes'

        else:
            half = num_list[i] // 2
            question = num_list[i]

            for item in range(half, min - 1, -1):
                if num_list[i] % item == 0:
                    answer = 'no'
                    break

                else:
                    answer = 'yes'

        ques_list.append(question)
        ques_list.append(answer)
        i += 1

    return ques_list


def brain_prime():
    user_name = welcome_user()
    prime_start()
    ques_answ_list = prime_ques_gen(min_num, max_num, amount_ques)
    check_win_list = question_answer(ques_answ_list)
    is_win(check_win_list, user_name)
