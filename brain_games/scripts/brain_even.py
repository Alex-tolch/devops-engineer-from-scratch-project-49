import random

from brain_games.common import run_game


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round():
    number = random.randint(1, 10000)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer


def main():
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_round,
    )


if __name__ == '__main__':
    main()
