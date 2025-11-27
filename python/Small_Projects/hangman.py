import random

def hangman():
    word_list = ['apple', 'orange', 'banana', 'pear']
    computer = random.choice(word_list)
    attempts = 15
    guessed_letters = []

    print("Welcome to hangman!")
    print("_ " * len(computer))

    while attempts > 0:

  # Validate input
        current_input = input("Enter your guess: ").lower()
        if len(current_input) != 1 or not current_input.isalpha():
            print("Enter a valid letter")
            continue

  # If already guessed
        if current_input in guessed_letters:
            print("You have already guessed this letter")
            continue

        guessed_letters.append(current_input)
  # If guess is correct
        if current_input in computer:
            print("correct guess")
        else:
            attempts -= 1
            print ("Your guess is not right")

  # Show current progress
        display = [letter if letter in guessed_letters else "_" for letter in computer]
        print(" ".join(display))
   # Check if player won
        if "_" not in display:
            print(f"You guessed it right: {computer}! You win!!")
            break
    else:
        print (f"Out of attempts, You loose 😢. Correct word is {computer}")


  

hangman() 