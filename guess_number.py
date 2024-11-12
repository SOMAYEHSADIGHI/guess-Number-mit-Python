# 1) user input => low and hight bound
# 2) random => [a, b]
# 3) loop => condition=> gusse_count => feedback
import random

try:
    low = int(input("Enter lower bound: \ n"))
    high = int(input("Enter high bound:  \n"))

except:
    print("please enter a valid number")

r = random.randint(low, high)

gusse_count = 5

while gusse_count > 0:

    try:
        new_guess_str = input(
            f"remained guess: {gusse_count} => Enter your next guess: \n"
        )
        new_guess = int(new_guess_str)

        if r == new_guess:
            print("Great! your duess is correct")
            break
        elif r > new_guess:
            print("Your duess is lower than selected number")
        else:
            print("Your duess is higher than selected number")
        gusse_count -= 1

    except:
        print("please enter a valid number")
