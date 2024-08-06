import random
from random import randint


MIN = 1
MAX = 15
DESCRIPTION = 'What is the result of the expression?'


def calculate(a, b, symbol):
    """
    Returns the result of an arithmetic operation
    Keyword arguments:
    a: int
    b: int
    symbol: str ('+', '-', '*')
    """
    if symbol == '+':
        result = a + b
    if symbol == '-':
        result = a - b
    if symbol == '*':
        result = a * b
    return result


def generate():
    """
    Returns a random arithmetic operation
    and the result of this operation
    """
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    actions_list = ['+', '-', '*']
    action = random.choice(actions_list)
    question = f'{a} {action} {b}'
    answer = calculate(a, b, action)
    return question, answer
