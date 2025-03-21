#  Author : Aayan Atif
#  Revison date : 21 March 2025
#  Program : Guess the number
#  Description : A program that is a game that makes the user guess the number!
#  Course Code: ICS3U0
#  VARIABLE DICTIONARY:
#  target_number (int) = Stores the randomly generated number between 1 and 100.
#  guess_count (int) = Tracks the number of guesses the user has made.
#  max_attempts (int) = The maximum number of guesses allowed (6).
#  user_guess (int) = Stores the number input by the user on each guess.

import random

# Generate a random number between 1 and 100
# This will be the number the user has to guess

target_number = random.randint(1, 100)  

guess_count = 0  # Initialize the guess count to track attempts
max_attempts = 6  # Maximum number of attempts allowed

# Output the game instructions to the user
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
print("Try to guess the number in at most", max_attempts, "attempts.")

# Loop to allow the user to guess up to 6 times
while guess_count < max_attempts:
    guess_count += 1  # Increase the guess count by 1
    
    # Ask user for their guess and convert input to an integer
    print("Guess #", guess_count, ":", sep="", end=" ")
    user_guess = int(input())
    
    # Puts the users guess and the correct number side by side and compares them
    if user_guess > target_number:
        print("Lower!")  # Hint: Guess a smaller number
    elif user_guess < target_number:
        print("Higher!")  # Hint: Guess a larger number
    else:
        print("Congratulations! You guessed the right number!")  # Correct guess message
        guess_count = max_attempts  # Set guess_count to max_attempts to end the game

# If the correct number has not been guessed, display the correct number
if user_guess != target_number:
    print("Sorry, you are out of guesses. The correct number was", target_number, ". Better luck next time!")
