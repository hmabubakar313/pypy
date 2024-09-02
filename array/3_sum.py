def three_summ(arr, target):
    pair = []
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            for z in range(y+1, len(arr)):
                if arr[x]+arr[y]+arr[z] == target:
                    pair.append((arr[x], arr[y], arr[z]))
                    return pair


print(three_summ([1, 4, 45, 6, 10, 8], 22))
