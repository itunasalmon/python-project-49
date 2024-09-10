#!/usr/bin/env python3
# file <brain_calc.py>

import prompt
from random import randint, choice
from operator import add, sub, mul


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print('What is the result of the expression?')

    round_count = 1
    min_number = 1
    max_number = 15

    while round_count <= 3:
        operand_one = randint(min_number, max_number)
        operand_two = randint(min_number, max_number)
        operation, operator = choice([
            (add, '+'),
            (sub, '-'),
            (mul, '*')])
        correct_answer = operation(operand_one, operand_two)
        question = f'{operand_one} {choice(operator)} {operand_two}'
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == correct_answer:
            print('Correct!')
            round_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {user_name}!")

    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
