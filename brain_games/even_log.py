from random import randint
from brain_games.cli import welcome_user


min_num = 1
max_num = 100
amount_num = 3


def even_greeting():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def rendom_num(min, max, amount):
    num_list = []
    i = 1
    while i <= amount:
        num_list.append(randint(min, max))
        i += 1
    return num_list


def is_even(number_list):
    check_list = [None, None, None]
    for item in number_list:
        print(f'Question: {item}')
        if item % 2 == 0:
            corr_answer = 'yes'
        else:
            corr_answer = 'no'

        user_answer = input('Your answer: ')

        if user_answer == corr_answer:
            check_list[0] = True
            print('Correct!')
        else:
            check_list[0] = False
            check_list[1] = user_answer
            check_list[2] = corr_answer
            return check_list

    return check_list


def is_win(ques_list, name):
    if ques_list[0] is True:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{ques_list[1]}' is wrong answer ;(. Correct answer was '{ques_list[2]}'.")
        print(f"Let's try again, {name}!")


def brain_even():
    user_name = welcome_user()
    even_greeting()
    rendom_list = rendom_num(min_num, max_num, amount_num)
    check_list = is_even(rendom_list)
    is_win(check_list, user_name)
