import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(rules: str, get_round):
    """Run a game: welcome, show rules, run rounds. get_round() -> (question, correct_answer)."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(rules)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_round()
        print(f'Question: {question}')
        user_answer_raw = prompt.string('Your answer: ')
        user_answer = user_answer_raw.strip()
        normalized_user = user_answer.lower()
        normalized_correct = correct_answer.strip().lower()

        if normalized_user != normalized_correct:
            print(f"'{user_answer_raw}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
