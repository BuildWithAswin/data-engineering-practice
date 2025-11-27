import random
def rock_paper():
    choices = ["rock", "paper", "scissors"]
    player_input = input("Enter the input: ").strip().lower()
    computer = random.choice(choices)


    if player_input == computer:
        print ("Its a tie 🤝 !")
    elif (player_input == "rock" and computer == "scissors") or \
        (player_input == "scissors" and computer == "paper") or \
            (player_input == "paper" and computer == "rock"):
                print ("You win 🥇!!")
    else:
        print("You loose 😢")


rock_paper()

