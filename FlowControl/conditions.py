age = int(input("Enter your age : "))
if 18 <= age <= 60:
    print("go to work")
else:
    if age < 18:
        print("go and play")
    else:
        print("go and take rest")
