import random
from qx.colors import color

low = int(input("\nLowest number: "))
high = int(input("Highest number: "))

num = random.randint(low, high)

# cheat
# print(num)

guess = int(input("\nGuess: "))

done = False
while not done:
    try:
        if guess == num:
            print(color.GREEN, "Win", color.ENDC)
            done = True
        elif guess > num:
            print(color.YELLOW, "Too high", color.ENDC)
            guess = int(input("\nGuess: "))
        elif guess < num:
            print(color.YELLOW, "Too low", color.ENDC)
            guess = int(input("\nGuess: "))
        else:
            print(color.RED, "Invalid Input", color.ENDC)
            guess = int(input("\nGuess: "))
    except:
        print("Invalid Input")
        guess = int(input("Guess: "))
