import random

def play_rps():
    """Plays a game of Rock Paper Scissors with the user."""
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_rps()
    while True:
        play_again = input("Play again? (yes/no): ").lower()
        if play_again == "yes":
            play_rps()
        else:
            print("Thanks for playing!")
            break