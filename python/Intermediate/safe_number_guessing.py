# safe number guessing using try/except
import random

random_integer = random.randint(0, 100)

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 0 or guess > 100:
            print("Enter a valid integer between 1-100")
            continue

        if random_integer > guess:
            print("Guess is too low!")
        elif random_integer < guess:
            print("Guess is too high!")
        else:
            print("You guessed it right!")
            break
    except ValueError:
        print("Invalid input ! Please enter valid digit between 0 to 100")
