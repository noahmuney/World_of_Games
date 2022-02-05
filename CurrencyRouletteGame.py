from random import randint
from currency_converter import CurrencyConverter
c = CurrencyConverter()


def get_money_interval(t, d):
    interval = (t - (5 - d), t + (5 - d))
    return interval


def is_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def get_guess_from_user(a):
    valid = False
    while not valid:
        guess = (input(f"Guess how many NIS {a} USD is worth:\n"))
        if is_float(guess):
            valid = True
            guess = float(guess)
        else:
            print("Invalid Input\nPlease enter a number.")
            valid = False
    return guess


def play(diff):
    amount = randint(1, 100)
    exact = c.convert(amount, 'USD', 'ILS')
    interval = get_money_interval(exact, diff)
    guess = get_guess_from_user(amount)
    if interval[0] < guess < interval[1]:
        print(f"You Win!\nThe exact answer was {exact}.")
        win = True
    else:
        print(f"You Lose!\nThe correct answer was {exact}.")
        win = False
    return win
