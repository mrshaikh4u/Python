# parrot_list = ["abc","sdf","Sdf"]
# parrot_list.append("sdfdfd")
# for parrot in parrot_list:
#     print(parrot)
#
# even_list = [2,4,6,8,10]
# odd_list = [1,3,5,7,9]
#
# numbers = even_list+odd_list
# numbers.sort()
#
# print(numbers)
# numbers_in_order = sorted(numbers)
#
# if numbers_in_order == numbers:
#     print("equal")
# else:
#     print("not equal")
#
# list = list()
# list2 = []
#
# if list == list2:
#     print("lists are equal")

# even = [2,4,6,8]
#
# sorted_even = list(even)
#
# print(sorted_even== even)
#
# print(sorted_even is even)
#
# even = [2,4,6,8]
# odd = [1,3,5,7]
# numbers = [even , odd]
# print(numbers)
#
# for number_set in numbers:
#     print(number_set,end="")
#     for number in number_set:
#         print(number)

menu=[]
menu.append(["asf","df","spam"])
menu.append(["asf","df","spam"])
menu.append(["asf","af"])
menu.append(["asf","df","spam"])
menu.append(["asf","rs"])

for item in menu:
    if "spam" not in item:
        for i in item:
            print(i,end="\t")
        print("\n")

