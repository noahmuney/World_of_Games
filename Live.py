import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play")


def load_game():
    valid_game = False
    while not valid_game:
        game = input("Please choose a game to play:\n"
                     "1. Memory Game - A sequence of numbers will appear for one second and you'll need to correctly "
                     "remember it\n"
                     "2. Guessing Game - Try to guess the computer's number\n"
                     "3. Currency Roulette - Try to guess the value of a random amount of USD in NIS\n Your choice: ")
        if game.isdigit() is True and 0 < int(game) < 4:
            valid_game = True
            game = int(game)
            if game == 1:
                print("You have selected The Memory Game")
            elif game == 2:
                print("You have selected The Guessing Game")
            elif game == 3:
                print("You have selected Currency Roulette")
        else:
            print("Invalid Input\nPlease enter a number between 1 and 3")
            valid_game = False
    valid_diff = False
    while not valid_diff:
        diff = input("Please select game difficulty from 1 to 5: ")
        if diff.isdigit() is True and 0 < int(diff) < 6:
            print(f"You have selected difficulty {diff}")
            valid_diff = True
            diff = int(diff)
        else:
            print("Invalid Input\nPlease enter a number between 1 and 5")
            valid_diff = False
    if game == 1:
        MemoryGame.play(diff)
    elif game == 2:
        GuessGame.play(diff)
    elif game == 3:
        CurrencyRouletteGame.play(diff)
