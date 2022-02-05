from random import sample
from time import sleep
from main_game import diff


def generate_sequence():
    seq = sample(range(0, 102), diff)
    return seq


def get_list_from_user():
    usr_list = [int(x) for x in input("What was the sequence?\n").split(', ')]
    return usr_list


def is_list_equal(a, b):
    if a == b:
        return True
    else:
        return False


def play():
    seq = generate_sequence()
    print(seq)
    sleep(0.7)
    print("\n" * 100)
    win = is_list_equal(get_list_from_user(), seq)
    if win is True:
        print("You Win!")
    else:
        print("You Lose!")
    return win

