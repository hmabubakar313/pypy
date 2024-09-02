def search_element(arr, target):
    for x, y in enumerate(arr):
        if y == target:
            return arr[x]
    return None


print(search_element([1, 2, 3], 2))

