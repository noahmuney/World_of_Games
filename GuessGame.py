from random import randint


def generate_number(diff):
    secret_number = randint(1, diff)
    return secret_number


def get_guess_from_user(diff):
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


def play(diff):
    a = generate_number(diff)
    b = get_guess_from_user(diff)
    win = compare_results(a, b)
    if win is True:
        print(f"You Win!\nThe answer was {a}")
    else:
        print(f"You Lose!\nThe answer was {a}")
    return win
