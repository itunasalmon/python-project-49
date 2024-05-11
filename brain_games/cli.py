#!/usr/bin/env python3
# file <cli.py>

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
