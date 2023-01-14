import random

choices = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)
    if player_choice == computer_choice:
        print("Tie!\n")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win!\n")
            player_wins += 1
        else:
            print("Computer wins!\n")
            computer_wins += 1
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!\n")
            player_wins += 1
        else:
            print("Computer wins!\n")
            computer_wins += 1
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win!\n")
            player_wins += 1
        else:
            print("Computer wins!\n")
            computer_wins += 1
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")

if player_wins == 3:
    print("You win the match!\n")
else:
    print("Computer wins the match!\n")