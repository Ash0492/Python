import random

while True:
    user_input = int(input("Please enter a number"))
    

    while user_input < 1 or user_input > 9:
        print("The entered number don't fall in the given range")
        user_input = int(input("Please enter a valid number in the given range"))
        break

    rand_input = random.randint(1,9)

    if user_input > rand_input:
        print("The number is greater")
    elif user_input < rand_input:
            print("The number is smaller")
    else:
            print("The number is exactly equal")

    print("Please type exit to stop this game")
    ans = input()

    if ans == 'exit':
            break
        
