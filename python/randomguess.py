import random
low=1
high=100
number=random.randint(low,high)
attempts=0
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {low} and {high}. Can you guess it?")
while True:
    guess=int(input("Enter your guess: "))
    attempts+=1
    if guess<number:
        print("Too low! Try again.")
    elif guess>number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break