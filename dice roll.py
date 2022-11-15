import random

attempts = 0
print("press a key to roll the dice")
input()

while True:
    numbers = ["1", "2", "3", "4", "5", "6"]
    roll = random.choice(numbers)
    print("roll: " + str(roll))
    attempts += 1
    if roll == "6":
        break
    input()


print("it took you " + str(attempts) + " attempts to roll a six")
input()