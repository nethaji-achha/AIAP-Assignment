def linear_search(arr, target):
    indexes = []
    for idx, val in enumerate(arr):
        if val == target:
            indexes.append(idx)
    return indexes

# Input list from user
input_str = input("Enter list elements separated by spaces: ")
arr = [int(x) for x in input_str.strip().split()]

# Input target to search
target = int(input("Enter element to search: "))

result = linear_search(arr, target)
if result:
    print(f"Element {target} found at indexes: {result}")
else:
    print(f"Element {target} not found in the list.")
