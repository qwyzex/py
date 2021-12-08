import random

low = int(input("Lowest number: "))
high = int(input("Highest number: "))

num = random.randint(low, high)

print(num)

guess = int(input("Guess: "))

done = False
while not done:
    try:
        if guess == num:
            print("Win")
            done = True
        elif guess > num:
            print("Too high")
            guess = int(input("Guess: "))
        elif guess < num:
            print("Too low")
            guess = int(input("Guess: "))
        else:
            print("Invalid Input")
            guess = int(input("Guess: "))
    except:
        print("Invalid")
        guess = int(input("Guess: "))
