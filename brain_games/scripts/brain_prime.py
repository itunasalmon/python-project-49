#!/usr/bin/env python3
# file <brain_prime.py>

from random import randint
import prompt


def is_prime(number):
    if number <= 1:
        return False

    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False

    return True


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    round_count = 1
    while round_count <= 3:
        number = randint(1, 200)
        question = number
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if is_prime(number) else 'no'

        if user_answer == correct_answer:
            print('Correct!')
            round_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")

    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
