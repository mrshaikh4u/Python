answer = 5
user_guess = int(input("Guess a number between 1 and 10 : "))
if user_guess == answer:
    print("you won")
else:
    if user_guess > answer:
        print("your guess is too high")
        user_guess= int(input("guess lower"))
        if user_guess == answer:
            print("you won")
        else:
            print("you lost")
    else:
        print("your guess is too low")
        user_guess= int(input("guess higher"))
        if user_guess == answer:
            print("you won")
        else:
            print("you lost")




