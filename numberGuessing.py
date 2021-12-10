import random
from qx.colors import color

low = int(input("Lowest number: "))
high = int(input("Highest number: "))

num = random.randint(low, high)

# cheat
# print(num)

guess = int(input("Guess: "))

done = False
while not done:
    try:
        if guess == num:
            print(color.GREEN, "Win", color.ENDC)
            done = True
        elif guess > num:
            print(color.YELLOW, "Too high", color.ENDC)
            guess = int(input("Guess: "))
        elif guess < num:
            print(color.YELLOW, "Too low", color.ENDC)
            guess = int(input("Guess: "))
        else:
            print(color.RED, "Invalid Input", color.ENDC)
            guess = int(input("Guess: "))
    except:
        print("Invalid Input")
        guess = int(input("Guess: "))
