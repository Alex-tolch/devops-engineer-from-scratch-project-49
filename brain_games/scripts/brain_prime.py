import random

from brain_games.common import run_game


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def get_round():
    number = random.randint(1, 50)
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer


def main():
    run_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        get_round,
    )


if __name__ == "__main__":
    main()
