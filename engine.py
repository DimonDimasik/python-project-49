from brain_games.cli import welcome_user


rounds = 3


def question_answer(ques_list):
    check_list = [None, None, None]

    print(f'Question: {ques_list[0]}')
    user_answer = input('Your answer: ')

    if user_answer == ques_list[1]:
        check_list[0] = True
        return check_list
    else:
        check_list[0] = False
        check_list[1] = user_answer
        check_list[2] = ques_list[1]
        return check_list


def win(name):
    print(f'Congratulations, {name}!')


def loose(wrong, correct, name):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.")
    print(f"Let's try again, {name}!")


def game_engine(module):
    user_name = welcome_user()
    i = 1
    module.start()
    while i <= rounds:
        ques_list = module.ques_gen(module.min_num, module.max_num)
        result_list = question_answer(ques_list)

        if result_list[0] is True and i < rounds:
            print('Correct!')
            i += 1

        elif result_list[0] is True and i == rounds:
            print('Correct!')
            win(user_name)
            break

        elif result_list[0] is False:
            loose(result_list[1], result_list[2], user_name)
            break
