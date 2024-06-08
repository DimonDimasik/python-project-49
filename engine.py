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
            print(f'Congratulations, {user_name}!')
            break

        elif result_list[0] is False:
            print(f"'{result_list[1]}' is wrong answer ;(. Correct answer was '{result_list[2]}'.")
            print(f"Let's try again, {user_name}!")
            break
