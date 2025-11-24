import random

def number_guess_game():
    high_score = None  # Tracks best (lowest) number of guesses in this session

    while True:
        number = random.randint(1, 100)
        max_attempts = 10
        attempts = 0

        print("\nWelcome to the Number Guessing Game!\n")
        print("I'm thinking of a number between 1 and 100.\n")
        print("You have" ,max_attempts, "attempts to guess it!\n")

        while attempts < max_attempts:
            user_input = input(f"Attempt {attempts + 1}: Enter your guess: ")
            
            # Input validation: only accept numbers
            if not user_input.isdigit():
                print("Please enter a valid number.")
                continue  # Ask again, attempt count unchanged

            guess = int(user_input)
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries!")
                if high_score is None or attempts < high_score:
                    high_score = attempts
                    print("🎉 NEW SESSION HIGH SCORE!")
                else:
                    print(f"Session best: {high_score} guesses.")
                break  # Exit while (user won)

        else:
            # If max_attempts used with no win
            print(f"Sorry, you're out of attempts. The number was {number}.")
            if high_score is not None:
                print(f"Session best score so far: {high_score} guesses.")

        # Play again option
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! See you next time!")
            break

number_guess_game()
