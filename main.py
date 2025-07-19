from random import randint



def main():

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.", end="\n\n")

    total_guesses = get_difficulty_level()
    print()
    print(f"You have {total_guesses} chances to guess the number.", end="\n\n")

    play_again = ""
    while play_again != "n":
        answer = randint(1, 100)
        play_game(total_guesses, answer)
        play_again = input("\nDo you want to play again? (y/n) ").lower()

    print("Thanks for playing!")



def get_difficulty_level():
    print("""Please choose a difficulty level:
    1. Easy (10 guesses)
    2. Medium (5 guesses)
    3. Hard ( 3 guesses)\n""")

    valid = False
    while not valid:
        try:
            level_choice = int(input("Enter your choice: "))
            if level_choice in range(1, 4):
                valid = True
        except ValueError:
            print("Please choose a valid difficulty level: 1, 2, or 3.")


    if level_choice == 1:
        print("\nYou chose Easy.\nLet's start the game!", end="\n\n")
        return 10
    elif level_choice == 2:
        print("\nYou chose Medium.\nLet's start the game!", end="\n\n")
        return 5
    else:
        print("\nYou chose Hard.\nLet's start the game!", end="\n\n")
        return 3

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