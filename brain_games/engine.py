from brain_games.cli import welcome_user


ROUNDS = 3


def win(name):
    print(f'Congratulations, {name}!')


def loose(wrong, correct, name):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.")
    print(f"Let's try again, {name}!")


def game_engine(module):
    user_name = welcome_user()
    i = 1
    module.start()
    while i <= ROUNDS:
        ques_list = module.question_answer()
        print(f'Question: {ques_list[0]}')
        user_answer = input('Your answer: ')

        if user_answer == ques_list[1]:
            print('Correct!')
            i += 1

        else:
            loose(user_answer, ques_list[1], user_name)
            break

    if user_answer == ques_list[1]:
        win(user_name)
