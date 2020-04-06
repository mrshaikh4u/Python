shopping = ["Sugar","Spam","Dress","Bread","Milk"]
found_at = None
if "Spam" in shopping:
    print("item found at {}".format(shopping.index("Spam")))

# for index in range(len(shopping)):
#     if shopping[index] == "Spam":
#         found_at = index
#     print(shopping[index])

print("found at : {}".format(found_at))