from random import randint

from main_game import diff


def generate_number():
    secret_number = randint(0, diff + 1)
    return secret_number


def get_guess_from_user():
    valid_guess = False
    while not valid_guess:
        guess = input(f"Please guess a number between 1 and {diff}: ")
        if guess.isdigit() is True and 0 < int(guess) < diff + 1:
            valid_guess = True
            guess = int(guess)
        else:
            print("Invalid Input")
            valid_guess = False
    return guess


def compare_results(a, b):
    if a == b:
        return True
    else:
        return False


def play():
    win = compare_results(generate_number(), get_guess_from_user())
    if win is True:
        print("You Win!")
    else:
        print("You Lose!")
    return win
