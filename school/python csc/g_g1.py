
import random 

rnd =  random.randint(1,3)
guess = int(input("Guess the number 1 - 3: "))
attempts = 1

while guess != rnd:

    if attempts == 3:
        print(f"Your guess has exceed 3 attempts, the correct guess is {rnd}")
        break
    
    
    if guess < rnd:
        print("Guess is lower")
    else:
        print("Guess is higher")
    guess = int(input("Guess the number 1 - 10: "))
    attempts += 1
    
else:
    print("You have won!!", rnd)
