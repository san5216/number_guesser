from random import randint
from enum import Enum


class DIFFICULTY(Enum):
    EASY = {"name": "Easy", "guesses": 10}
    MEDIUM = {"name": "Medium", "guesses": 5}
    HARD = {"name": "Hard", "guesses": 3}



class Game:
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    def __init__(self):
        self.secret_number = None
        self.total_guesses = 0
        self.guesses_made = 0
        self.difficulty_level = None

    def display_welcome(self):
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}.", end="\n\n")

    def get_difficulty_level(self):
        print("Please choose a difficulty level:")
        for i, difficulty in enumerate(DIFFICULTY, start=1):
            print(f"{i}. {difficulty.value["name"]} ({difficulty.value["guesses"]} chances)")

        while True:
            try:
                level_choice = int(input("\nChoose a level (1, 2, or 3): "))
                if 1 <= level_choice <= 3:
                    difficulty = list(DIFFICULTY)[level_choice - 1]
                    print(f"\nGreat! You have selected the {difficulty.value['name']} difficulty level.")
                    print("Let's start the game!", end="\n\n")
                    return difficulty
                else:
                    print("Please choose 1, 2, or 3.")
            except ValueError:
                print("Please choose a valid difficulty level: 1, 2, or 3.")


    def run(self):
        self.display_welcome()
        self.difficulty_level = self.get_difficulty_level()


def main():

    game = Game()
    game.run()

    # total_guesses = get_difficulty_level()
    # print()
    # print(f"You have {total_guesses} chances to guess the number.", end="\n\n")
    #
    # play_again = ""
    # while play_again != "n":
    #     answer = randint(1, 100)
    #     play_game(total_guesses, answer)
    #     play_again = input("\nDo you want to play again? (y/n) ").lower()
    #
    # print("Thanks for playing!")

def play_game(total_guesses, secret_number):

    guesses_made = 1
    while guesses_made <= total_guesses:

        valid = False
        while not valid:
            try:
                guess = int(input("Enter your guess: "))
                if guess in range(1, 101):
                    valid = True
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a number between 1 and 100.")

        if guess > secret_number:
            print(f"\nIncorrect! The number is less than {guess}")
        elif guess < secret_number:
            print(f"\nIncorrect! The number is greater than {guess}")
        else:
            print(f"You guessed the secret number in {guesses_made} guesses!")
            return

        remaining = total_guesses - guesses_made
        if remaining > 0:
            print(f"\nYou have {total_guesses - guesses_made} guesses remaining.")
        else:
            print(f"\nYou are out of guesses! The secret number was {secret_number}.")

        guesses_made += 1


if __name__ == '__main__':
    main()