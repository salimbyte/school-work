# n = 4; k = 2
# print(n+1)
# print(n-1)
# print(n+k)

# def y(x):
#     result = x**2 - 5*x + 11
#     return result

# y = y(x=2)
# print(y)

# n = 7
# n = 15
# n = -3
# if (n < 10):
#     if (n > 0):
#         print("The number is positive")
#     else:
#         print("the number is negative")
# else:
#     print("the number is greater than 10")

# result = []

# for x in range(-6, 6):
#     y = 4*x*2 - 12
#     result.append(y)
# print(result)


# n = -5
# while (n < 0):
#     print("The integer you entered is negative")
#     n = int(input("Enter a non-negative integer: "))
# print("The number is entered is positive")



# n = 10
# while (n > 0):
#     n /= 2
#     print(n*n)
#     n = int(input("Enter a number greater than 0: "))

# mylist = ["orange", "apple", "mango"]

# mylist.pop(1)
# print(mylist)

# mylist.remove("apple")
# print(mylist)

# def sum_of_list(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n 
#     return sum

# result = sum_of_list([1, 2, 3, 8, 9, 10, 40])
# print(result)


# mylist = [1, 2, 3, 4, 5]
# print(mylist[1:4])

# variable = 3

# n = int(input("Enter a value: "))

# if variable == n:
#     print("Variable is the same as n ")
# else:
#     print("Variable and n are not the same")

# for n in range(1, 11):
#     print(n)



# x = int(input("Enter your value of x: "))

# if x > 0:
#     print("x is positive")
# else:
#     print("x is negative")

# n = int(input("Enter a number: "))

# if n % 2 == 0:
#     print("n is Even")
# else:
#     print("n is Odd")


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible")
# else:
#     print("You are not eligible")

# mylist = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 10, 10]]

# for i in mylist:
#     for j in i:
#         print(j, end=" ")



import random

rnd = random.randint(1, 10)
guess = int(input("Enter your guess: "))
attempts = 1

while rnd != guess:
    if attempts == 3:
        print("You have exceeded 3 attempts")
        break
    
    if guess > rnd:
        print("You guess is higher")
    else:
        print("Your guess is lower")

    guess = int(input("Enter your guess: "))
    attempts += 1
else:
    print("You have won!")