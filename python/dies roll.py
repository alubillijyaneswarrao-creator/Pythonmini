import random 
choice ={1,2,3,4,5,6}
score=0
option = random.choice(list(choice))
print(option)
if option >= 4:
    score += 1
    print("You win")
else:
    print("You lose")
print(f"Your score is: {score}")