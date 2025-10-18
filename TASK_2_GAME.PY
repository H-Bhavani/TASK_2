#Task2: Number Guessing Game

import random

#to generate the secret number
secret_number=random.randint(1,100)

#intializing the variables
count=0
number=0
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I have selected a number between 1 and 100.")
print("try to guess it!")

#loop until the player guesses the number corectly 
while number != secret_number:
    try:
        number=int(input("Enter your guess:"))
        count += 1

        if number == secret_number:
            print(f"Correct! You guessed the number in {count} tries.")
        elif number > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print("Too low! Try a bigger number.")
    except ValueError:
        print("Please enter a valid number!")  #handles invalid input 

print("Thanks for playing! Goodbye!")