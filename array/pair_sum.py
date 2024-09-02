def pair_sum(l,target):
    for x in range(len(l)):
        for y in range(x+1, len(l)):
            if l[x] + l[y] == target:
                return True
    return False

print(pair_sum([0, -1, 2, -3, 1],target=-2))