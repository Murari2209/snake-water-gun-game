import random

# Choices
choices = ["snake", "water", "gun"]

# Computer choice
computer = random.choice(choices)

# User input
user = input("Enter your choice (snake/water/gun): ").lower()

if user not in choices:
    print("Invalid choice! Please choose snake, water, or gun.")
else:
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a draw!")

    elif (
        (user == "snake" and computer == "water") or
        (user == "water" and computer == "gun") or
        (user == "gun" and computer == "snake")
    ):
        print("You win!")

    else:
        print("Computer wins!")
