def find_max(l):
    if len(l) == 0:
        return None  

    max_item = l[0] 
    for x in l:
        if x > max_item:
            max_item = x
    return max_item

print(find_max([1, 2, 3, 4, 5, 6, 7]))