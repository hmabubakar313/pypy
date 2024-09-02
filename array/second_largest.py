def second_largest(l):
    for x in l:
        if l[0] > l[1]:
            largest = l[1]
            second_largest = l[0]
    return second_largest

print(second_largest([12, 35, 1, 10, 34, 1]))