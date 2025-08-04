import random

youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

youstr = input("Enter Your choice (s for Snake, w for Water, g for Gun): ").lower()

computer = random.choice([-1,0,1])
you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a Draw")
else:
    if computer == -1 and you == 1:
        print("You Win!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You Win!")
    elif computer == 0 and you == -1:
        print("You Win!")
    elif computer == 0 and you == 1:
        print("You Lose!")
    else:
        print("Something went Wrong!")
