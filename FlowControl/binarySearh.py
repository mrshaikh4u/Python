list = list(range(1, 20))
low = 0
high = len(list) - 1

to_search = 19

while low <= high:
    mid = low + ((high - low) // 2)
    if list[mid] == to_search:
        print(f"found at index {mid}")
        break
    if to_search > list[mid]:
        low = mid + 1
    else:
        high = mid
else:
    print("number not found")
