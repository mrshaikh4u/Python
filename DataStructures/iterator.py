# # # # string = "1234568890"
# # # # str_iterator = iter(string)
# # # # size = len(string)
# # # # for i in range (0,size):
# # # #     print(next(str_iterator))
# # # #
# # # # even = range(0,10,2)
# # # # for i in even:
# # # #     print(i)
# # #
# # # revesredstr = str(reversed("python is very powerfull language"))
# # #
# # # for char in revesredstr:
# # #     print(char,end="")
# # #
# # # print("now printing correctly")
# # #
# # # print(revesredstr[::-1])
# # # # for char in range(::-1)
# # #
# # # # print(revesredstr)
# # #
# # # # sevens = range(7,10000,7)
# # # # for j in sevens:
# # # #     print(j,end="\t")
# # o= range(0,100,4)
# # print(o) #  range(0,100,4)
# # p=o[::5] # range(0,100,5)
# # print(p)
# # for i in p:
# #     print(i)
# #
# # a=b=c=d = 10
# # print(c)
# # print(a)
# #
# # tupple = "as","sdf",123,"df"
# #
# # print(tupple)
# a,b = 10,12
# print("a {}".format(a))
# print("b {}".format(b))
#
# a,b=b,a
# print("a {}".format(a))
# print("b {}".format(b))
#
#
# tupple_packed = 1,2,3, (("a"),("b"),("c"))
# one , two , three , a,b,c = tupple_packed
# print(one)
# print(two)
# print(three)
# print(a)
# print(b)
# print(c)
#
details = 1,2,3,("sdf",1,"Sdf")
num1 ,num2, num3 , tracks= details
print(num1)
print(num2)
print(num3)
output=""
for string in tracks:
    output+=str(string)

print(output)



