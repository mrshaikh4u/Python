list = [10,12,31,60]
for i in list:
    if i%8 == 0:
        print("number is unaccepted")
        break
else:
    print("loop terminated gracefully")