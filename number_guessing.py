"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""


import random

def guess_number(low, high, num_attempts):
    """
    This function generates a pseudo-random integer within a given inclusive range and allows the user a certain number
    of attempts to guess it. It prints the range and number of attempts to the user, then asks for a guess repeatedly.
    Non-numeric guesses are handled gracefully without crashing and count as incorrect guesses. If the user guesses
    correctly at any attempt, the function returns True. If all guesses are incorrect, it returns False.

    :param low: The lower bound of the range in which the pseudo-random number is generated.
    :param high: The upper bound of the range in which the pseudo-random number is generated.
    :param num_attempts: The number of attempts the user is given to guess the correct number.
    :return: True if the user guesses correctly in any attempt, False otherwise.
    """
    # Generate a random number within the given range
    target_number = random.randint(low, high)

    print(f"Guess the number between {low} and {high}. You have {num_attempts} attempts.")

    # Loop through the number of allowed attempts
    for attempt in range(num_attempts):
        try:
            # Get user input and attempt to convert it to an integer
            guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
            # Check if the guess is correct
            if guess == target_number:
                print("Congratulations! You guessed the number correctly.")
                return True
            else:
                print("Wrong guess. Try again!")
        except ValueError:
            # Handle non-numeric input
            print("That's not a valid number. Please try to enter a valid number.")

    # If no guesses were correct after all attempts, return False
    print("Sorry, all your guesses were incorrect.")
    return False
