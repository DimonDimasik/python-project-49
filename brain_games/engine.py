from brain_games.cli import welcome_user


ROUNDS = 3


def win(name):
    """
    Displays congratulations to the player
    Keyword arguments:
    name: str
    """
    print(f'Congratulations, {name}!')


def loose(wrong, correct, name):
    """
    Displays a message about the player's loss
    Keyword arguments:
    wrong: str
    correct: str
    name: str
    """
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.")
    print(f"Let's try again, {name}!")


def game_engine(module):
    """
    Controls the rounds of the game. Displays a question and accepts the
    user's answer and compares it with the correct answer. If the answer
    is wrong, the game ends; if the answer is correct, it continues until
    the last round.
    Keyword arguments:
    module: module
    """
    user_name = welcome_user()
    i = 1
    print(module.DESCRIPTION)
    while i <= ROUNDS:
        ques_list = module.generate()
        print(f'Question: {ques_list[0]}')
        user_answer = input('Your answer: ')

        if user_answer == str(ques_list[1]):
            print('Correct!')
            if i == 3:
                win(user_name)
            i += 1

        else:
            loose(user_answer, ques_list[1], user_name)
            break
