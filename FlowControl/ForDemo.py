number = input("please enter any number with sperators : ")
digits=""
for char in number:
    if char.isnumeric():
        digits+=char
print(digits)
