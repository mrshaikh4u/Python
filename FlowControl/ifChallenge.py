name = input("Enter your name : ")
age = int(input("Hi {} ,Enter your age : ".format(name)))
if 18 <= age < 30:
    print("Hey {}!, Welcome to the holiday".format(name))
else:
    print("Hey {} , you are not eligible for this holiday".format(name))