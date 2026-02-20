import random

from brain_games.common import run_game

MIN_LENGTH = 5
MAX_LENGTH = 10


def make_progression(start: int, step: int, length: int) -> list[int]:
    return [start + index * step for index in range(length)]


def get_round():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(1, 50)
    step = random.randint(1, 50)
    progression = make_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    parts = []
    for i, number in enumerate(progression):
        if i == hidden_index:
            parts.append("..")
        else:
            parts.append(str(number))
    question = " ".join(parts)
    return question, correct_answer


def main():
    run_game(
        "What number is missing in the progression?",
        get_round,
    )


if __name__ == "__main__":
    main()
