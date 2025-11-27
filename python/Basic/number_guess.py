import random
num = random.randint(1, 100)
attempt = 0
while True:
    guess = input("Please enter your guess: ")
    if not guess.isdigit():
        print("Enter a valid number")
        continue
    guess = int(guess)
    attempt += 1

    if guess < num:
        print("Number entered is too low")
    elif guess > num:
        print("Number entered is too high")
    else:
        print("You guessed it right")
        break
