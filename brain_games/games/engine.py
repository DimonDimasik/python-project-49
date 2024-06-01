from brain_games.cli import welcome_user


def calc_start():
    print('What is the result of the expression?')


def even_start():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def gcd_start():
    print('Find the greatest common divisor of given numbers.')


def prime_start():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def progress_start():
    print('What number is missing in the progression?')


def question_answer(ques_list):
    i = 0
    check_list = [None, None, None]
    while i <= 4:
        print(f'Question: {ques_list[i]}')
        user_answer = input('Your answer: ')
        if user_answer == ques_list[i + 1]:
            check_list[0] = True
            print('Correct!')
            i += 2
        else:
            check_list[0] = False
            check_list[1] = user_answer
            check_list[2] = ques_list[i + 1]
            return check_list
    return check_list


def is_win(ques_list, name):
    if ques_list[0] is True:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{ques_list[1]}' is wrong answer ;(. Correct answer was '{ques_list[2]}'.")
        print(f"Let's try again, {name}")


def game_engine(ques_gen, min, max, amount, start):
    user_name = welcome_user()
    start()
    ques_answ_list = ques_gen(min, max, amount)
    check_win_list = question_answer(ques_answ_list)
    is_win(check_win_list, user_name)
