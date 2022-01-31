def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play")


def load_game():
    global game, diff
    answer = input("Please choose a game to play:\n"
                   "1. Memory Game - A sequence of numbers will appear for one second and you'll need to correctly "
                   "remember it\n"
                   "2. Guessing Game - Try to guess the computer's number\n"
                   "3. Currency Roulette - Try to guess the value of a random amount of USD in ILS\n Your choice: ")
    if answer == "1":
        game = "memory"
        print("You have selected The Memory Game")
    elif answer == "2":
        game = "guess"
        print("You have selected The Guessing Game")
    elif answer == "3":
        game = "roulette"
        print("You have selected Currency Roulette")
    else:
        print("Invalid Input\nPlease choose a number between 1 and 3")
        load_game()
    valid = False
    while not valid:
        diff = input("Please select game difficulty from 1 to 5: ")
        if diff.isdigit() is True and 0 < int(diff) < 6:
            print(f"You have selected difficulty {diff}")
            valid = True
        else:
            print("Invalid Input\nPlease enter a number between 1 and 5")
            valid = False

    return game, diff

