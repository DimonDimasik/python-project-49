import random
from random import randint


MIN = 1
MAX = 15


def start():
    print('What is the result of the expression?')


def calculation(expression):
    result = eval(expression)
    return str(result)


def question_answer():
    quest_list = []
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    actions_list = ['+', '-', '*']
    action = random.choice(actions_list)
    question = f'{a} {action} {b}'
    answer = calculation(question)
    quest_list.append(question)
    quest_list.append(answer)
    return quest_list
