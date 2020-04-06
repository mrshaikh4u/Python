inputset = input("Enter input string : ")
vowels = frozenset("aeiou")
output = list()
for char in inputset:
    if char not in vowels:
        output.append(char)
print(sorted(output))
