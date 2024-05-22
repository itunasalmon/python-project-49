#!/usr/bin/env python3
# file <brain_even.py>

from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    round_count = 1
    min_number = 1
    max_number = 1000

    while round_count <= 3:
        question = randint(min_number, max_number)
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if not user_answer == correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
        else:
            print('Correct!')
            round_count += 1
    print(f'Congratulations, {user_name}!')
