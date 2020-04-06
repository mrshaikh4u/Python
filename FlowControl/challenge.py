print("Hey there please choose an option : ")
print("1 : learn python")
print("2 : learn Java")
print("3 : Go Swimming")
print("4 : have dinner")
print("0 : Exit")
option = None
while option!=0:
    option = int(input())
    print("you have selected : {} ".format(option))
else:
    print("you have exited")