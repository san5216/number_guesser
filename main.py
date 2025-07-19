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

    def get_valid_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if self.MIN_NUMBER <= guess <= self.MAX_NUMBER:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Please enter a number between 1 and 100.")

    def display_hint(self, guess):

        if guess > self.secret_number:
            print(f"\nIncorrect! The number is less than {guess}")
        else:
            print(f"\nIncorrect! The number is greater than {guess}")

    def display_remaining_guesses(self):

        remaining = self.total_guesses - self.guesses_made
        if remaining > 0:
            print(f"\nYou have {remaining} guess{"es" if remaining != 1 else ""} remaining.\n")

    def play_round(self):
        self.secret_number = randint(self.MIN_NUMBER, self.MAX_NUMBER + 1)
        self.guesses_made = 0
        self.total_guesses = self.difficulty_level.value["guesses"]

        print(f"You have {self.total_guesses} chances to guess the number.", end="\n\n")

        while self.guesses_made < self.total_guesses:

            guess = self.get_valid_guess()
            self.guesses_made += 1

            if guess == self.secret_number:
                print(f"You guessed the secret number in {self.guesses_made} guesses!")
                return True

            self.display_hint(guess)

            if self.guesses_made < self.total_guesses:
                self.display_remaining_guesses()

        print(f"\nYou are out of guesses! The secret number was {self.secret_number}.")
        return False

    def play_again(self):

        while True:
            play_again = input("\nDo you want to play again? (y/n) ").lower().strip()

            if play_again in ["y", "yes"]:
                return True
            elif play_again in ["n", "no"]:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    def run(self):
        self.display_welcome()
        self.difficulty_level = self.get_difficulty_level()

        while True:
            self.play_round()

            if not self.play_again():
                break


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
