testcase = int(input())
phonebook = dict()
for i in range(0,testcase):
    inputlist  = list(str(input()).split(' '))
    name = inputlist[0]
    number = inputlist[1]
    phonebook.update({name:number})
print(phonebook)
while True:
    try:
        name = str(input())
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Not found")
    except EOFError as error:
        pass