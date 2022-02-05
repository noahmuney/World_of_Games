from random import sample
from time import sleep


def generate_sequence(diff):
    seq = sample(range(0, 102), diff)
    return seq


def get_list_from_user():
    usr_list = [int(x) for x in input("What was the sequence?\n"
                                      "If you remember, enter the numbers separated by a comma.\n").split(', ')]
    return usr_list


def is_list_equal(a, b):
    if a == b:
        return True
    else:
        return False


def play(diff):
    print("Get Ready!\nThe game will start in 3 seconds.")
    sleep(3)
    seq = generate_sequence(diff)
    print(seq)
    sleep(1)
    print("\n" * 100)
    try:
        win = is_list_equal(get_list_from_user(), seq)
    except ValueError:
        win = False
    if win is True:
        print("You Win!")
    else:
        print(f"You Lose!\nThe sequence was {seq}.")
    return win
