def is_sorted(l):
    if len(l) == 0:
        return None
    for x in range(len(l) -1):
        if l[x] > l[x+1]:
            return False
    return True
        



print(is_sorted([5,2,4,3,1,8]))

