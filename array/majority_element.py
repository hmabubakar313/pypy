def majority_element(l):
    if not l:
        return None
    counts = {}
    for x in l:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    for num, count in counts.items():
        if count > len(l) // 2:
            return num
    return None


print(majority_element([1, 2, 1]))