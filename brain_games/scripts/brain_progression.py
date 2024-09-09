#!/usr/bin/env python3
# file <brain_progression.py>

from random import choice, randint
import prompt


def progression_generation():
    first_item = randint(1, 30)
    progression_length = randint(5, 10)
    progression_step = randint(1, 15)
    progression = [first_item]

    while len(progression) <= progression_length:
        next_item = progression[-1] + progression_step
        progression.append(next_item)

    return progression


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')

    round_count = 1
    while round_count <= 3:
        progression = progression_generation()
        random_index = choice(progression)
        correct_answer = random_index
        question = list(map(
            lambda x: x if x != random_index else '..', progression))
        question = ' '.join(str(item) for item in question)

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == correct_answer:
            print('Correct!')
            round_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
