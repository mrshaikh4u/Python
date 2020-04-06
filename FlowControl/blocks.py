name = input("Hi,What is your name : ")
age = int(input("how old are you {0} : ".format(name)))

if(age<18):
    print("you are not old enough to vote")
    print("please come back after {}".format(18-age))
elif(age==900):
    print("you are too old")
