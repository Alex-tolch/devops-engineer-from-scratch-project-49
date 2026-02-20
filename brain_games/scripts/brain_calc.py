import random

from brain_games.common import run_game

OPERATIONS = [
    ('+', lambda a, b: a + b),
    ('-', lambda a, b: a - b),
    ('*', lambda a, b: a * b),
]


def get_round():
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    op_symbol, op_func = random.choice(OPERATIONS)
    question = f'{a} {op_symbol} {b}'
    correct_answer = str(op_func(a, b))
    return question, correct_answer


def main():
    run_game(
        'What is the result of the expression?',
        get_round,
    )


if __name__ == '__main__':
    main()
