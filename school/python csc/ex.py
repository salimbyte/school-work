
try:
    num = int(input("Enter the number to check for"))
except ValueError:
    print("You can only use numbers")
else:

    if num > 6:
        print("Out of range")
    else:
            
        for i in range(0, 6):
            if i == num:
                break

            print(i, "", end="")