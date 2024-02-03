# This is a number guessing game where the user is given 5 tries to guess a number from 1 to 10
import random
import sys
# Generate a random number
random_number = random.randint(1,10)
tries_allowed = 5
# Game Loop
while tries_allowed != 0:
    # Show tries left
    print(f"Number of tries left = {tries_allowed}")
    # User guesses the number
    predicted_number = int(input("Enter your Guess, Integer from 1 to 10 : "))
    if (random_number == predicted_number):
        # Game over
        print("You Win!")
        sys.exit()        
    else:
        if predicted_number > random_number:
            print("Guess is too high") 
        elif predicted_number < random_number:
            print("Guess is too low")
    # Decrease the number of tries
    tries_allowed -= 1
# Game over
print(f"You Lose!, the number was {random_number}, better luck next time!")
