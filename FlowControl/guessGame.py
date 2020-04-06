import random
highest = 10
answer = random.randint(1,highest)
print(f"correct answer is {answer}")
while True:
    print(f"Please guess a number between 1 and {highest} : ")
    user_guess = int(input())
    if user_guess == answer:
        print("Hurrey you won")
        break
    elif user_guess > answer:
        print("please guess lesser number")
    else:
        print("please guess higher nuber")

print("game over")