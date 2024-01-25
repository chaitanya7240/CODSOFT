import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    elif (
        (user_choice == "rock" and computer_choice == scissors) or
        (user_choice == "paper" and computer_choice == rock) or
        (user_choice == "scissors" and computer_choice == paper)
    ):
        return "You win"
    else:
        return "You lose"

outcomes = [rock, paper, scissors]
t = True

while t:
    computer_choice = random.choice(outcomes)

    user_choice = input("Choose rock, paper, or scissors: ").lower()

    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input().lower()

    print(f"You chose:\n{globals()[user_choice]}")
    print(f"Computer chose:\n{computer_choice}")

    result = winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again not in ['y', 'yes']:
        t = False

print("Thank you for playing")
