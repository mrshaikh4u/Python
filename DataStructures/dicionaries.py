fruit = {"apple":"good for health",
         "grape":"small sweet fruit",
         "orange":"good for vitamin c",
         "mango":"good in test"}
# print(fruit)
key="passionFruite"
value="new fruit in fruit basket"
fruit.update({key:value})

print(fruit)


#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# # for f in ordered_keys:
# #     print(f+" -     "+fruit.get(f))
# #
# # for f in sorted(fruit.keys()):
# #     print(f+"-"+fruit.get(f))
#
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomator"] = "sdffdsf"
# # print(fruit_keys)
#
#
# #
# # while True:
# #     dict_key = input("Enter name of fruit : ")
# #     if dict_key=="Quit":
# #         break
# #     description = fruit.get(dict_key,"we dont have "+dict_key)
# #     print(description)
#
#
#

# print(fruit.items())
#
# tupples = tuple(fruit.items())
# for t in tupples:
#     print(t)