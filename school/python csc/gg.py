# generate the random number
import random

rnd = random.randint(0, 10)

# ask the player for guess
guess = int(input("Enter your guess: "))
attempts = 1

while rnd != guess:
    if attempts == 3:
        print("Tries is exsausted", "the correct guess is", rnd)
        break

    if guess < rnd:
        print("your guess is Lower")
    else:
        print("Your guess is Higher")
    
    guess = int(input("Enter your guess: "))
    attempts += 1

else:
    print("You have won!!")    
    