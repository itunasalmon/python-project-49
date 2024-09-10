#!/usr/bin/env python3
# file <brain_gcd.py>

from random import randint
import prompt


def find_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')

    round_count = 1

    while round_count <= 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        question = f'{first_number} {second_number}'
        correct_answer = find_gcd(first_number, second_number)
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
