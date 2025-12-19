import random
options = ["Rock", "Paper", "Scissors"]
score = [0,0]
rounds = 10
for i in range(rounds):
    print(f"Round {i+1}")
    user = input("Enter rock,paper,scissors:").capitalize()
    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You win this round!")
        score[0] += 1
    else:
        print("Computer wins this round!")
        score[1] += 1
print(f"Final Score - You: {score[0]}, Computer: {score[1]}")