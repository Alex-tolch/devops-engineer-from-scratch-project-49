import math
import random

from brain_games.common import run_game


def get_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'{a} {b}'
    correct_answer = str(math.gcd(a, b))
    return question, correct_answer


def main():
    run_game(
        'Find the greatest common divisor of given numbers.',
        get_round,
    )


if __name__ == '__main__':
    main()
