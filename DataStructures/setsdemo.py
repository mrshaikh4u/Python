# animals = {"","","",""}

# animalset = set(range(1,100,2))


even = range(1,10)
squares=list()

for item in even:
    squares.append(item*item)

# print(list(even))
# print(squares)
#
# print(set(even))
# print(sorted(set(squares)))
# print(sorted(set(even).union(set(squares))))
# print(sorted(set(even).intersection(set(squares))))
# print(sorted(set(even) & set(squares)))


big_set = {1,2,3,4,5,6,7,8,9,0}
small_set = {4,5,6}
if small_set.issubset(big_set):
    print("small set is sub set of big")


# print(big_set.difference(small_set))
# print(big_set)
# print(small_set)
# # print(big_set.difference_update(small_set))
#
# print("big set")
# print(big_set)
#
# print("small set")
# print(small_set)
#
# print("symetric difference")
# print(big_set.symmetric_difference(small_set))
# print(big_set)
# big_set.discard()
