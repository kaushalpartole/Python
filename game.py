import random
options = ["Rock", "Paper", "Scissors"]
computerChoice = random.choice(options)

userChoice = input("Enter Rock, Paper or Scissors - ").capitalize()
print(f"User choice is {userChoice}") 
print(f"Computer choice is {computerChoice}")

if userChoice == computerChoice:
    print("it's a tie")

elif userChoice == "Rock" and computerChoice == "Scissors":
    print("you win!")
elif userChoice == "Paper" and computerChoice == "Rock":
    print("you win!")
elif userChoice == "Scissors" and computerChoice == "Paper":
    print("you win!")

else:
    print("you loose!")