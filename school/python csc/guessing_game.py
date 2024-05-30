"""
guessing game using python.

flow:
    using random module, we pick a radom int 0 - 10
    then we take input x from a user

    we then check for if that input is not equal to radom value we pick
        check if number of tries didnt exceed 3
            ask user to reguess again 
            and then add the number of tries + 1 (max 3)
            return to the look
        else:
            prompt user to have failed.
"""

import random

num: int = random.randint(1, 10)
tries: int = 1
guess: int 
def get_guess() -> int:
    try:
        guess: int = int(input("Enter your guess: "))
    except ValueError:
        print("you can only input an integer")
        get_guess()
    else:
        return guess

guess: int = get_guess()
print(guess)
while guess != num:
    if tries == 3:
        print(f"Your guess has exceed 3 attempts, the correct guess is {num}")
        break
    else:
        tries += 1
        if guess != num:
            print(guess)
            if guess < num:
                print("Guess is lower")
            else:
                print("Guess is highter")
            guess = get_guess()
            continue
        else:
            break
else:
    print(f"You have won!!! the guess is {guess}")