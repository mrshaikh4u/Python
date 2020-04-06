testcase = int(input())
for i in range(testcase):
    input_str = str(input())
    for j in range(len(input_str)):
        if (j%2) == 0:
            print(f"{input_str[j]}",end ="")
    else:
        print(" ",end="")
    for k in range(len(input_str)):
        if (k%2) != 0:
            print(f"{input_str[k]}",end ="")


# Hacker
# Rank