import random

# 1 = Snake, -1 = Water, 0 = Gun

def play_game():
    computer = random.choice([1, -1, 0])

    youstr = input("Enter your choice (s/w/g): ").lower()

    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    if youstr not in youDict:
        print("Invalid input! Please enter s, w or g.")
        return

    user = youDict[youstr]

    print(f"You chose {reverseDict[user]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == user:
        print("It's a Draw")

    elif (computer == -1 and user == 1) or \
         (computer == 1 and user == 0) or \
         (computer == 0 and user == -1):
        print("You Win ")

    else:
        print("You Lose")


play_game()