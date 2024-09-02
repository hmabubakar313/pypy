def sum_of_pairs(l1, target):
    pairs = []
    for x in range(len(l1)):
        for y in range(x + 1, len(l1)):
            if l1[x] + l1[y] == target:
                pairs.append((l1[x], l1[y]))
    return pairs




print(sum_of_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
